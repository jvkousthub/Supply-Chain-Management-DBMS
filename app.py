from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database
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

@app.before_request
def before_request():
    if not db.connection:
        if not db.connect():
            flash('Database connection failed. Check credentials and Oracle service.', 'error')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/suppliers')
def suppliers():
    suppliers = db.get_all_suppliers()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/suppliers/add', methods=['GET', 'POST'])
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
            flash('Supplier added successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Failed to add supplier', 'error')
    
    return render_template('add_supplier.html')

@app.route('/suppliers/edit/<int:supplier_id>', methods=['GET', 'POST'])
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
            flash('Supplier updated successfully', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('Failed to update supplier', 'error')
    
    suppliers = db.execute_query("SELECT * FROM suppliers WHERE supplier_id = :1", (supplier_id,))
    return render_template('edit_supplier.html', supplier=suppliers[0] if suppliers else None)

@app.route('/suppliers/delete/<int:supplier_id>')
def delete_supplier(supplier_id):
    if db.delete_supplier(supplier_id):
        flash('Supplier deleted successfully', 'success')
    else:
        flash('Failed to delete supplier', 'error')
    return redirect(url_for('suppliers'))

@app.route('/products')
def products():
    products = db.get_all_products()
    return render_template('products.html', products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        supplier_id = int(request.form['supplier_id'])
        price = float(request.form['price'])
        description = request.form['description']
        
        if db.add_product(name, category, supplier_id, price, description):
            flash('Product added successfully', 'success')
            return redirect(url_for('products'))
        else:
            flash('Failed to add product', 'error')
    
    suppliers = db.get_all_suppliers()
    return render_template('add_product.html', suppliers=suppliers)

@app.route('/products/delete/<int:product_id>')
def delete_product(product_id):
    if db.delete_product(product_id):
        flash('Product deleted successfully', 'success')
    else:
        flash('Failed to delete product', 'error')
    return redirect(url_for('products'))

@app.route('/warehouses')
def warehouses():
    warehouses = db.get_all_warehouses()
    return render_template('warehouses.html', warehouses=warehouses)

@app.route('/warehouses/add', methods=['GET', 'POST'])
def add_warehouse():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        city = request.form['city']
        capacity = int(request.form['capacity'])
        manager = request.form['manager']
        phone = request.form['phone']
        
        if db.add_warehouse(name, location, city, capacity, manager, phone):
            flash('Warehouse added successfully', 'success')
            return redirect(url_for('warehouses'))
        else:
            flash('Failed to add warehouse', 'error')
    
    return render_template('add_warehouse.html')

@app.route('/inventory')
def inventory():
    inventory = db.get_inventory_status()
    return render_template('inventory.html', inventory=inventory)

@app.route('/inventory/low-stock')
def low_stock():
    items = db.get_low_stock()
    return render_template('low_stock.html', items=items)

@app.route('/inventory/update/<int:inventory_id>', methods=['POST'])
def update_inventory(inventory_id):
    quantity = int(request.form['quantity'])
    if db.update_inventory(inventory_id, quantity):
        flash('Inventory updated successfully', 'success')
    else:
        flash('Failed to update inventory', 'error')
    return redirect(url_for('inventory'))

@app.route('/orders')
def orders():
    orders = db.get_all_orders()
    return render_template('orders.html', orders=orders)

@app.route('/orders/create', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        supplier_id = int(request.form['supplier_id'])
        warehouse_id = int(request.form['warehouse_id'])
        delivery_date = request.form['delivery_date']
        
        if db.create_order(supplier_id, warehouse_id, delivery_date):
            flash('Order created successfully', 'success')
            return redirect(url_for('orders'))
        else:
            flash('Failed to create order', 'error')
    
    suppliers = db.get_all_suppliers()
    warehouses = db.get_all_warehouses()
    return render_template('create_order.html', suppliers=suppliers, warehouses=warehouses)

@app.route('/orders/<int:order_id>')
def order_details(order_id):
    order = db.execute_query("SELECT * FROM orders WHERE order_id = :1", (order_id,))
    details = db.get_order_details(order_id)
    return render_template('order_details.html', order=order[0] if order else None, details=details)

@app.route('/orders/status/<int:order_id>', methods=['POST'])
def update_order_status(order_id):
    status = request.form['status']
    if db.update_order_status(order_id, status):
        flash('Order status updated', 'success')
    else:
        flash('Failed to update status', 'error')
    return redirect(url_for('orders'))

@app.route('/analytics')
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
