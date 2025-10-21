from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import Database
from auth import AuthManager, login_required, role_required, get_permissions
import os
from pathlib import Path

env_path = Path('.') / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

DB_USER = os.getenv('DB_USER', 'your_username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
DB_DSN = os.getenv('DB_DSN', 'localhost:1521/XEPDB1')

print(f"Connecting to Oracle as: {DB_USER}@{DB_DSN}")

db = Database(DB_USER, DB_PASSWORD, DB_DSN)
auth = AuthManager(db)

@app.before_request
def before_request():
    if not db.connection:
        if not db.connect():
            flash('Database connection failed. Check credentials and Oracle service.', 'error')

@app.context_processor
def inject_permissions():
    if 'role' in session:
        return {'permissions': get_permissions(session['role'])}
    return {'permissions': None}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = auth.authenticate(username, password)
        
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['full_name'] = user['full_name']
            session['email'] = user['email']
            session['role'] = user['role']
            
            auth.log_action(user['user_id'], user['username'], 'LOGIN', 'app_users', 
                          ip_address=request.remote_addr)
            
            flash(f'Welcome back, {user["full_name"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    username = session.get('username')
    user_id = session.get('user_id')
    
    if user_id and username:
        auth.log_action(user_id, username, 'LOGOUT', 'app_users', ip_address=request.remote_addr)
    
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/suppliers')
@login_required
def suppliers():
    suppliers = db.get_all_suppliers()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/suppliers/add', methods=['GET', 'POST'])
@role_required('ADMIN', 'MANAGER')
def add_supplier():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        rating = float(request.form['rating'])
        
        if db.add_supplier(name, contact, email, phone, address, city, country, rating):
            auth.log_action(session['user_id'], session['username'], 'ADD SUPPLIER', 
                          'suppliers', ip_address=request.remote_addr)
            flash('Supplier added successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Failed to add supplier', 'error')
    
    return render_template('add_supplier.html')

@app.route('/suppliers/edit/<int:supplier_id>', methods=['GET', 'POST'])
@role_required('ADMIN', 'MANAGER')
def edit_supplier(supplier_id):
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        rating = float(request.form['rating'])
        
        if db.update_supplier(supplier_id, name, contact, email, phone, address, city, country, rating):
            auth.log_action(session['user_id'], session['username'], 'UPDATE SUPPLIER', 
                          'suppliers', supplier_id, ip_address=request.remote_addr)
            flash('Supplier updated successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Failed to update supplier', 'error')
    
    suppliers = db.execute_query("SELECT * FROM suppliers WHERE supplier_id = :1", (supplier_id,))
    return render_template('edit_supplier.html', supplier=suppliers[0] if suppliers else None)

@app.route('/suppliers/delete/<int:supplier_id>')
@role_required('ADMIN')
def delete_supplier(supplier_id):
    if db.delete_supplier(supplier_id):
        auth.log_action(session['user_id'], session['username'], 'DELETE SUPPLIER', 
                      'suppliers', supplier_id, ip_address=request.remote_addr)
        flash('Supplier deleted successfully', 'success')
    else:
        flash('Failed to delete supplier', 'error')
    return redirect(url_for('suppliers'))

@app.route('/products')
@login_required
def products():
    products = db.get_all_products()
    return render_template('products.html', products=products)

@app.route('/products/add', methods=['GET', 'POST'])
@role_required('ADMIN', 'MANAGER')
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        supplier_id = int(request.form['supplier_id'])
        price = float(request.form['price'])
        description = request.form['description']
        
        if db.add_product(name, category, supplier_id, price, description):
            auth.log_action(session['user_id'], session['username'], 'ADD PRODUCT', 
                          'products', ip_address=request.remote_addr)
            flash('Product added successfully', 'success')
            return redirect(url_for('products'))
        else:
            flash('Failed to add product', 'error')
    
    suppliers = db.get_all_suppliers()
    return render_template('add_product.html', suppliers=suppliers)

@app.route('/products/delete/<int:product_id>')
@role_required('ADMIN')
def delete_product(product_id):
    if db.delete_product(product_id):
        auth.log_action(session['user_id'], session['username'], 'DELETE PRODUCT', 
                      'products', product_id, ip_address=request.remote_addr)
        flash('Product deleted successfully', 'success')
    else:
        flash('Failed to delete product', 'error')
    return redirect(url_for('products'))

@app.route('/warehouses')
@login_required
def warehouses():
    warehouses = db.get_all_warehouses()
    return render_template('warehouses.html', warehouses=warehouses)

@app.route('/warehouses/add', methods=['GET', 'POST'])
@role_required('ADMIN', 'MANAGER')
def add_warehouse():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        city = request.form['city']
        capacity = int(request.form['capacity'])
        manager = request.form['manager']
        phone = request.form['phone']
        
        if db.add_warehouse(name, location, city, capacity, manager, phone):
            auth.log_action(session['user_id'], session['username'], 'ADD WAREHOUSE', 
                          'warehouses', ip_address=request.remote_addr)
            flash('Warehouse added successfully', 'success')
            return redirect(url_for('warehouses'))
        else:
            flash('Failed to add warehouse', 'error')
    
    return render_template('add_warehouse.html')

@app.route('/inventory')
@login_required
def inventory():
    inventory = db.get_inventory_status()
    return render_template('inventory.html', inventory=inventory)

@app.route('/inventory/low-stock')
@login_required
def low_stock():
    items = db.get_low_stock()
    return render_template('low_stock.html', items=items)

@app.route('/inventory/update/<int:inventory_id>', methods=['POST'])
@role_required('ADMIN', 'MANAGER', 'WAREHOUSE')
def update_inventory(inventory_id):
    quantity = int(request.form['quantity'])
    if db.update_inventory(inventory_id, quantity):
        auth.log_action(session['user_id'], session['username'], 'UPDATE INVENTORY', 
                      'inventory', inventory_id, ip_address=request.remote_addr)
        flash('Inventory updated successfully', 'success')
    else:
        flash('Failed to update inventory', 'error')
    return redirect(url_for('inventory'))

@app.route('/orders')
@login_required
def orders():
    orders = db.get_all_orders()
    return render_template('orders.html', orders=orders)

@app.route('/orders/create', methods=['GET', 'POST'])
@role_required('ADMIN', 'MANAGER')
def create_order():
    if request.method == 'POST':
        supplier_id = int(request.form['supplier_id'])
        warehouse_id = int(request.form['warehouse_id'])
        delivery_date = request.form['delivery_date']
        
        order_id = db.create_order(supplier_id, warehouse_id, delivery_date)
        if order_id:
            auth.log_action(session['user_id'], session['username'], 'CREATE ORDER', 
                          'orders', order_id, ip_address=request.remote_addr)
            flash('Order created successfully', 'success')
            return redirect(url_for('orders'))
        else:
            flash('Failed to create order', 'error')
    
    suppliers = db.get_all_suppliers()
    warehouses = db.get_all_warehouses()
    return render_template('create_order.html', suppliers=suppliers, warehouses=warehouses)

@app.route('/orders/<int:order_id>')
@login_required
def order_details(order_id):
    order = db.execute_query("SELECT * FROM orders WHERE order_id = :1", (order_id,))
    details = db.get_order_details(order_id)
    return render_template('order_details.html', order=order[0] if order else None, details=details)

@app.route('/orders/status/<int:order_id>', methods=['POST'])
@role_required('ADMIN', 'MANAGER')
def update_order_status(order_id):
    status = request.form['status']
    if db.update_order_status(order_id, status):
        auth.log_action(session['user_id'], session['username'], 'UPDATE ORDER STATUS', 
                      'orders', order_id, ip_address=request.remote_addr)
        flash('Order status updated', 'success')
    else:
        flash('Failed to update status', 'error')
    return redirect(url_for('orders'))

@app.route('/analytics')
@login_required
def analytics():
    category_data = db.get_inventory_by_category()
    top_suppliers = db.get_top_suppliers()
    warehouse_util = db.get_warehouse_utilization()
    order_status = db.get_orders_by_status()
    reorder_needed = db.get_products_needing_reorder()
    
    return render_template('analytics.html', 
                         category_data=category_data,
                         top_suppliers=top_suppliers,
                         warehouse_util=warehouse_util,
                         order_status=order_status,
                         reorder_needed=reorder_needed)

@app.route('/users')
@role_required('ADMIN')
def users():
    users = auth.get_all_users()
    return render_template('users.html', users=users)

@app.route('/users/add', methods=['GET', 'POST'])
@role_required('ADMIN')
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        email = request.form.get('email', '')
        role = request.form['role']
        
        if auth.create_user(username, password, full_name, email, role):
            auth.log_action(session['user_id'], session['username'], f'CREATED USER: {username}', 
                          'app_users', ip_address=request.remote_addr)
            flash(f'User {username} created successfully', 'success')
            return redirect(url_for('users'))
        else:
            flash('Failed to create user - username may already exist', 'error')
    
    return render_template('add_user.html')

@app.route('/users/toggle/<int:user_id>', methods=['POST'])
@role_required('ADMIN')
def toggle_user(user_id):
    if auth.toggle_user_status(user_id):
        auth.log_action(session['user_id'], session['username'], f'TOGGLED USER STATUS', 
                      'app_users', user_id, ip_address=request.remote_addr)
        flash('User status updated', 'success')
    else:
        flash('Failed to update user status', 'error')
    return redirect(url_for('users'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
