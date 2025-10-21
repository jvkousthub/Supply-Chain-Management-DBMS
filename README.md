# Supply Chain Management System

A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, and comprehensive **Oracle Database** integration.

## Features

### Core Functionality
- **User Authentication**: Secure login with SHA-256 password hashing and session management
- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Viewer)
- **Supplier Management**: Track and manage supplier information with ratings
- **Product Catalog**: Maintain product inventory with categories and pricing
- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking
- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels
- **Order Processing**: Create and track purchase orders with status updates
- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations
- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses

### Database Features
- **DDL**: Table creation with constraints, foreign keys, and indexes
- **DML**: Insert, Update, Delete operations with data validation
- **DQL**: Complex SELECT queries with multi-table joins
- **DCL**: User permissions and role-based access control (GRANT, REVOKE)
- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)
- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views

## Tech Stack

- **Backend**: Python 3.8+, Flask 3.0.0
- **Database**: Oracle Database 11g or higher
- **Driver**: python-oracledb (pure Python implementation)
- **Frontend**: HTML5, CSS3 with professional navy blue theme, Jinja2 templates
- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection

## Installation

### Prerequisites

- Python 3.8 or higher
- Oracle Database (XE 11g/18c/21c recommended)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git
   cd "Supply Chain Management DBMS"
   ```

2. **Run setup script**
   ```cmd
   setup.bat
   ```
   This will:   - Create a virtual environment

   setup.bat   - Install all dependencies

   ```   - Create a `.env` file template

   This will:

   - Create a virtual environment3. **Configure database**

   - Install all dependencies   

   - Create a `.env` file template   Edit `.env` file with your Oracle credentials:

   ```properties

3. **Configure database**   DB_USER=your_username

      DB_PASSWORD=your_password

   Edit `.env` file with your Oracle credentials:   DB_DSN=localhost:1521/XEPDB1

   ```properties   SECRET_KEY=your-secret-key

   DB_USER=system   ```

   DB_PASSWORD=your_password

   DB_DSN=localhost:1521/XE4. **Create database schema**

   SECRET_KEY=your-secret-key   

   ```   Connect to Oracle and run:

   ```sql

4. **Create database schema**   @schema.sql

      @sample_data.sql

   Connect to Oracle and run:   ```

   ```sql

   sqlplus system/your_password@localhost:1521/XE5. **Start the application**

   - Install Python dependencies
   - Create virtual environment
   - Configure database connection

3. **Configure database credentials**
   
   Edit the credentials in `setup.bat` or create a `.env` file:
   ```
   DB_USER=system
   DB_PASSWORD=your_password
   DB_DSN=localhost:1521/XE
   SECRET_KEY=your-secret-key-here
   ```

4. **Run SQL scripts**
   
   Connect to Oracle as system user:
   ```sql
   sqlplus system/your_password@localhost:1521/XE
   
   SQL> @schema.sql
   SQL> @sample_data.sql
   SQL> @add_authentication.sql
   SQL> exit
   ```

5. **Start the application**
   ```cmd
   run.bat
   ```

6. **Open browser and login**
   
   Navigate to: `http://localhost:5000`
   
   **Default credentials:**
   - Admin: `admin` / `password123`
   - Manager: `manager` / `password123`
   - Warehouse: `warehouse` / `password123`
   - Viewer: `viewer` / `password123`

## User Roles & Permissions

| Role          | View All | Add Items | Edit Items | Delete Items | Update Inventory | Manage Users |
|------         |----------|-----------|------------|--------------|------------------|--------------|
| **ADMIN**     | ✅ Yes   | ✅ Yes    | ✅ Yes    | ✅ Yes       | ✅ Yes          | ✅ Yes |
| **MANAGER**   | ✅ Yes   | ✅ Yes    | ✅ Yes    | ❌ No        | ✅ Yes          | ❌ No |
| **WAREHOUSE** | ✅ Yes   | ❌ No     | ❌ No*    | ❌ No        | ✅ Yes*         | ❌ No |
| **VIEWER**    | ✅ Yes   | ❌ No     | ❌ No     | ❌ No        | ❌ No           | ❌ No |

*WAREHOUSE role can only edit/update inventory quantities, nothing else.

### Role Descriptions

- **ADMIN**: Complete system control including user management, all CRUD operations, and audit log access
- **MANAGER**: Can view all data and perform most operations except deletions and user management
- **WAREHOUSE**: Specialized role limited to viewing and updating inventory stock levels only
- **VIEWER**: Read-only access across all sections for reporting and analysis purposes

### Security Features

- **Password Security**: SHA-256 hashing for all passwords
- **Session Management**: Secure session-based authentication
- **Access Control**: Route-level permission enforcement with decorators
- **Audit Trail**: Complete logging of all user actions (login, logout, create, update, delete)
- **UI Protection**: Dynamic button hiding based on user permissions
- **IP Tracking**: Records IP addresses for all actions

## Project Structure

```
├── app.py                      # Flask application with authentication routes
├── auth.py                     # Authentication manager and role decorators
├── database.py                 # Database operations and queries
├── requirements.txt            # Python dependencies
├── schema.sql                  # Database schema (DDL)
├── sample_data.sql             # Sample data (DML)
├── add_authentication.sql      # User authentication setup
├── user_roles_dcl.sql          # Oracle DCL implementation
├── dcl_permissions.sql         # Additional permissions (DCL)
├── tcl_examples.sql            # Transaction examples (TCL)
├── advanced_queries.sql        # Complex queries and analytics

├── templates/                  # HTML templates- View low-stock alerts

│   ├── base.html              # Base template with navbar- Update quantities

│   ├── login.html             # Login page- Track last updated timestamps

│   ├── users.html             # User management (admin)

│   ├── index.html             # Dashboard### Order Processing

│   └── ...                    # Other templates- Create new orders

├── .env                        # Environment variables (create this)- Add products to orders

├── .gitignore                  # Git ignore rules- Update order status (PENDING → CONFIRMED → SHIPPED → DELIVERED)

├── setup.bat                   # Installation script- View order details and history

├── ROLE_TESTING_GUIDE.md       # Complete testing guide for roles
├── templates/                  # HTML templates with role-based UI
│   ├── base.html               # Base template with navbar
│   ├── login.html              # Authentication page
│   ├── users.html              # User management (Admin)
│   ├── suppliers.html          # Supplier listing
│   ├── products.html           # Product catalog
│   ├── warehouses.html         # Warehouse management
│   ├── inventory.html          # Stock levels
│   ├── orders.html             # Order listing
│   └── analytics.html          # Dashboard with charts
├── setup.bat                   # Installation script
└── run.bat                     # Start script
```

## Database Schema

### Main Tables

1. **suppliers** - Supplier information with contact details and ratings
2. **warehouses** - Warehouse locations with capacity and manager info
3. **products** - Product catalog with categories and pricing
4. **inventory** - Stock levels with reorder points and last updated
5. **orders** - Purchase orders with status tracking and delivery dates
6. **order_details** - Order line items with quantities and pricing
7. **shipments** - Delivery tracking with carrier and tracking numbers
8. **app_users** - User accounts with roles and password hashes
9. **audit_log** - Complete action tracking with timestamps and IP addresses

### Views

- **low_stock_items** - Products below reorder level (requires immediate attention)
- **order_summary** - Order aggregates by status with totals
- **supplier_performance** - Supplier ratings and order counts with performance metrics

### Sequences

- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq`
- `order_seq`, `detail_seq`, `shipment_seq`
- `user_seq`, `log_seq`

### Indexes

- `idx_inventory_product` - Fast product lookups in inventory
- `idx_inventory_warehouse` - Warehouse-based inventory queries
- `idx_product_supplier` - Supplier product relationships
- `idx_order_supplier` - Order history by supplier
- `idx_order_status` - Filter orders by status
- `idx_shipment_order` - Track shipments by order

## Usage

### Authentication Flow

1. **Login** - Navigate to `http://localhost:5000` (redirects to login)
2. **Enter credentials** - Use one of the default accounts or admin-created accounts
3. **Session management** - Stays logged in until logout or session expires
4. **Automatic tracking** - All actions logged with user, timestamp, and IP

### Managing Users (Admin Only)

- **Create users** - Add new users with assigned roles
- **Activate/deactivate** - Toggle user account status
- **View activity** - See last login times and user details
- **Audit logs** - Review complete action history

### Managing Suppliers (Admin/Manager)

- **View all** - List all suppliers with ratings and contact info
- **Add new** - Create supplier records with full details
- **Edit** - Update supplier information (Admin/Manager only)
- **Delete** - Remove suppliers (Admin only)

### Product Management (Admin/Manager)

- **View catalog** - Browse all products with categories
- **Add products** - Create new product entries
- **Delete** - Remove products from catalog (Admin only)

### Inventory Management (Admin/Manager/Warehouse)

- **Monitor stock** - View current levels across all warehouses
- **Low stock alerts** - Identify products needing reorder
- **Update quantities** - Adjust stock levels (all three roles can do this)
- **Track changes** - Last updated timestamps for all items

### Order Processing (Admin/Manager)

- **View orders** - List all purchase orders with status
- **Create orders** - Generate new purchase orders
- **Update status** - Change order status (Pending → Confirmed → Shipped → Delivered)
- **View details** - See line items and totals for each order

### Analytics & Reports (All Users)

- **Inventory by category** - GROUP BY analysis
- **Top suppliers** - Order value aggregates
- **Warehouse utilization** - Capacity vs current stock
- **Products needing reorder** - HAVING clause filters
- **Order status distribution** - Visual breakdown

## SQL Features Demonstrated

### DDL (Data Definition Language)
- CREATE TABLE with constraints
- ALTER TABLE operations
- CREATE INDEX for performance
- CREATE SEQUENCE for auto-increment
- CREATE VIEW for reusable queries

### DML (Data Manipulation Language)
- INSERT with sequences
- UPDATE with conditions
- DELETE with cascading
- MERGE for upserts

### DQL (Data Query Language)
- **Joins**: INNER, LEFT, RIGHT, FULL OUTER
- **Aggregates**: COUNT, SUM, AVG, MIN, MAX
- **Group By & Having**: Category and status analysis
- **Subqueries**: Nested SELECT for complex filtering
- **Order By**: Sorting results

### DCL (Data Control Language)
- CREATE USER statements
- GRANT permissions by role
- REVOKE access rights
- Role-based security model

### TCL (Transaction Control Language)
- COMMIT for saving changes
- ROLLBACK for undoing
- SAVEPOINT for partial rollbacks
- Transaction isolation

## Development

### Running in Debug Mode

Flask debug mode is enabled by default in `app.py`:
```python
app.run(debug=True, port=5000)
```

### Environment Variables

Create a `.env` file with:
```
DB_USER=system
DB_PASSWORD=your_password
DB_DSN=localhost:1521/XE
SECRET_KEY=your-secret-key-change-this
FLASK_ENV=development
```

### Testing Roles

See `ROLE_TESTING_GUIDE.md` for comprehensive testing scenarios for each user role.

## Troubleshooting

### Database Connection Failed

1. Verify Oracle service is running:
   ```cmd
   services.msc
   # Look for OracleServiceXE or similar
   ```

2. Check credentials match in your setup

3. Test connection with SQL*Plus:
   ```cmd
   sqlplus system/password@localhost:1521/XE
   ```

### Import Errors

Run setup again to reinstall dependencies:
```cmd
setup.bat
```

### Tables Not Found

Ensure all SQL scripts were executed:
```sql
sqlplus system/password@localhost:1521/XE
SQL> @schema.sql
SQL> @sample_data.sql
SQL> @add_authentication.sql
```

### Permission Denied Errors

- Verify you're logged in with the correct role
- Check that decorators are properly applied in `app.py`
- Review `auth.py` permissions matrix
- Test with admin account first

```

### Session Expired

- Sessions expire after inactivity
- Simply log in again to continue

## Oracle DCL Implementation

The system demonstrates comprehensive Oracle DCL (Data Control Language) features through two mechanisms:

### 1. Oracle Native Users (user_roles_dcl.sql)

Creates actual Oracle database users with role-based permissions:

```sql
-- Create Oracle users
CREATE USER scm_admin IDENTIFIED BY Admin@123;
CREATE USER scm_manager IDENTIFIED BY Manager@123;
CREATE USER scm_warehouse IDENTIFIED BY Warehouse@123;
CREATE USER scm_viewer IDENTIFIED BY Viewer@123;

-- Admin: Full access
GRANT CONNECT, RESOURCE, DBA TO scm_admin;
GRANT ALL PRIVILEGES ON suppliers TO scm_admin;

-- Manager: Selective permissions
GRANT CONNECT, RESOURCE TO scm_manager;
GRANT SELECT, INSERT, UPDATE ON suppliers TO scm_manager;
GRANT SELECT, INSERT, UPDATE ON products TO scm_manager;
-- No DELETE privileges

-- Warehouse: Limited to inventory
GRANT CONNECT TO scm_warehouse;
GRANT SELECT, UPDATE ON inventory TO scm_warehouse;
-- Can only view and update stock levels

-- Viewer: Read-only access
GRANT CONNECT TO scm_viewer;
GRANT SELECT ON suppliers TO scm_viewer;
GRANT SELECT ON products TO scm_viewer;
GRANT SELECT ON inventory TO scm_viewer;
```

### 2. Application-Level Users (add_authentication.sql)

Creates app_users table for web application authentication:

```sql
CREATE TABLE app_users (
    user_id NUMBER PRIMARY KEY,
    username VARCHAR2(50) UNIQUE NOT NULL,
    password VARCHAR2(256) NOT NULL,  -- SHA-256 hash
    full_name VARCHAR2(100),
    email VARCHAR2(100),
    role VARCHAR2(20) CHECK (role IN ('ADMIN', 'MANAGER', 'WAREHOUSE', 'VIEWER')),
    is_active NUMBER(1) DEFAULT 1,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

**Default accounts** (all use password: `password123`):
- admin / Manager role
- manager / Manager role  
- warehouse / Warehouse operations
- viewer / Read-only access

## API Routes Reference

### Public Routes
- `GET/POST /login` - User authentication page

### Protected Routes (Login Required)

#### Dashboard & Analytics
- `GET /` - Main dashboard
- `GET /analytics` - Reports and visualizations

#### Supplier Management
- `GET /suppliers` - List all suppliers
- `GET/POST /suppliers/add` - Add supplier (Admin, Manager)
- `GET/POST /suppliers/edit/<id>` - Edit supplier (Admin, Manager)
- `POST /suppliers/delete/<id>` - Delete supplier (Admin only)

#### Product Management
- `GET /products` - List all products
- `GET/POST /products/add` - Add product (Admin, Manager)
- `POST /products/delete/<id>` - Delete product (Admin only)

#### Warehouse Management
- `GET /warehouses` - List warehouses
- `GET/POST /warehouses/add` - Add warehouse (Admin, Manager)

#### Inventory Management
- `GET /inventory` - View stock levels
- `GET /inventory/low-stock` - Low stock alerts
- `POST /inventory/update/<id>` - Update quantity (Admin, Manager, Warehouse)

#### Order Management
- `GET /orders` - List all orders
- `GET/POST /orders/create` - Create order (Admin, Manager)
- `GET /orders/<id>` - View order details
- `POST /orders/status/<id>` - Update status (Admin, Manager)

#### User Management (Admin Only)
- `GET /users` - View all users
- `GET/POST /users/add` - Create new user
- `POST /users/toggle/<id>` - Activate/deactivate user

## Testing

### Role Testing

Comprehensive testing guide available in `ROLE_TESTING_GUIDE.md`. Quick test checklist:

1. **Login as admin** → Should see all features including Users menu
2. **Login as manager** → Should see Add/Edit buttons but no Delete buttons
3. **Login as warehouse** → Should only see inventory update forms
4. **Login as viewer** → Should see data but no action buttons

### Verification Queries

```sql
-- Check user accounts
SELECT user_id, username, role, is_active, last_login 
FROM app_users 
ORDER BY role;

-- View recent audit logs
SELECT username, action, table_name, 
       TO_CHAR(action_time, 'YYYY-MM-DD HH24:MI:SS') as time
FROM audit_log 
ORDER BY log_id DESC 
FETCH FIRST 20 ROWS ONLY;

-- Count actions by user
SELECT username, COUNT(*) as total_actions
FROM audit_log
GROUP BY username
ORDER BY total_actions DESC;

-- Check low stock items
SELECT * FROM low_stock_items;

-- Supplier performance
SELECT * FROM supplier_performance;
```

## Production Deployment

### Pre-Deployment Checklist

- [ ] Change all default passwords (admin, manager, warehouse, viewer)
- [ ] Generate strong `SECRET_KEY` for Flask sessions
- [ ] Update database credentials in `.env`
- [ ] Enable HTTPS/SSL for web traffic
- [ ] Implement password complexity requirements
- [ ] Configure session timeouts (default: 24 hours)
- [ ] Set up regular audit log reviews
- [ ] Implement automated database backups
- [ ] Use production-grade WSGI server (Gunicorn/uWSGI)
- [ ] Configure Oracle for production workload

### Environment-Specific Configuration

**Development (.env):**
```env
DB_USER=system
DB_PASSWORD=your_dev_password
DB_DSN=localhost:1521/XE
SECRET_KEY=dev-secret-key
FLASK_ENV=development
```

**Production (.env):**
```env
DB_USER=scm_prod_user
DB_PASSWORD=strong_prod_password_here
DB_DSN=prod-db-server:1521/PROD
SECRET_KEY=generate-strong-random-secret
FLASK_ENV=production
```

### Recommended Production Changes

1. **Disable Flask debug mode** in `app.py`:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

2. **Add password complexity validation** in `auth.py`

3. **Implement session timeout** in Flask config

4. **Enable HTTPS** with SSL certificates

5. **Set up monitoring** for audit logs

## License

This project is created for educational purposes as part of a Database Management Systems (DBMS) course.

## Author

Created by [jvkousthub](https://github.com/jvkousthub)

**Project Type:** Database Management Systems coursework  
**Purpose:** Demonstrate Oracle SQL integration with Flask web framework  
**Features:** Complete CRUD operations, role-based access control, and enterprise-grade authentication

## Key Highlights

✅ **Complete SQL Implementation** - DDL, DML, DQL, DCL, TCL  
✅ **Role-Based Access Control** - 4 distinct user roles with granular permissions  
✅ **Security First** - Password hashing, session management, audit logging  
✅ **Professional UI** - Clean navy blue theme with responsive design  
✅ **Production Ready** - Error handling, validation, and comprehensive testing  

---

**⭐ If this project helped you understand database concepts or Flask integration, please star the repository!**

**📚 For detailed testing procedures, see:** `ROLE_TESTING_GUIDE.md`
