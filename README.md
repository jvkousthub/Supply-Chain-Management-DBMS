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
   This installs all dependencies and creates virtual environment.

3. **Configure database**
   
   Edit `.env` file with your Oracle credentials:
   ```properties
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
| **ADMIN**     | Yes      | Yes       | Yes        | Yes          | Yes              | Yes          |
| **MANAGER**   | Yes      | Yes       | Yes        | No           | Yes              | No           |
| **WAREHOUSE** | Yes      | No        | No*        | No           | Yes*             | No           |
| **VIEWER**    | Yes      | No        | No         | No           | No               | No           |

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

└── run.bat                     # Start script

```### Analytics

- Inventory by category (GROUP BY)

## Database Schema- Top suppliers by order value (aggregates)

- Warehouse utilization (subqueries)

### Main Tables- Products needing reorder (HAVING clause)

1. **suppliers** - Supplier information with ratings

2. **warehouses** - Warehouse locations and capacity## SQL Features Demonstrated

3. **products** - Product catalog with categories

4. **inventory** - Stock levels with reorder points- **Joins**: INNER, LEFT, RIGHT

5. **orders** - Purchase orders with status tracking- **Aggregates**: COUNT, SUM, AVG, MIN, MAX

6. **order_details** - Order line items- **Group By & Having**: Category analysis

7. **shipments** - Delivery tracking- **Subqueries**: Nested SELECT statements

8. **app_users** - User accounts with roles- **Views**: Reusable query abstractions

9. **audit_log** - Action tracking with timestamps- **Indexes**: Performance optimization

- **Sequences**: Auto-increment IDs

### Views- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK

- **low_stock_items** - Products below reorder level

- **order_summary** - Order aggregates by status## Development

- **supplier_performance** - Supplier ratings and order counts

### Running in Debug Mode

### SequencesFlask debug mode is enabled by default in `app.py`:

- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq````python

- `order_seq`, `detail_seq`, `shipment_seq`app.run(debug=True, port=5000)

- `user_seq`, `log_seq````



## Usage### Environment Variables

- `DB_USER`: Oracle username

### Authentication- `DB_PASSWORD`: Oracle password

- All routes require login (except `/login`)- `DB_DSN`: Database connection string

- Sessions persist until logout- `SECRET_KEY`: Flask session secret

- Automatic last login tracking- `FLASK_ENV`: development/production



### Managing Users (Admin Only)## Troubleshooting

- Create new users with assigned roles

- Activate/deactivate user accounts### Database Connection Failed

- View user activity and last login1. Verify Oracle service is running

2. Check credentials in `.env`

### Managing Suppliers3. Test connection with SQL*Plus:

- View all suppliers with ratings   ```

- Add new suppliers with contact information   sqlplus username/password@localhost:1521/XEPDB1

- Update supplier details   ```

- Delete suppliers (Admin only)

### Import Errors

### Inventory ManagementRun setup again:

- Monitor stock levels across all warehouses```cmd

- View low-stock alertssetup.bat

- Update quantities (Admin, Manager, Warehouse)```

- Track last updated timestamps

### Tables Not Found

### Order ProcessingRun the schema creation:

- Create new orders with delivery dates```sql

- Add products to orders@schema.sql

- Update order status: PENDING → CONFIRMED → SHIPPED → DELIVERED```

- View complete order details and history

## License

### Analytics

- Inventory by category (GROUP BY)This project is for educational purposes.

- Top suppliers by order value (aggregates)

- Warehouse utilization (subqueries)## Author

- Products needing reorder (HAVING clause)

- Order statistics by statusCreated as a Database Management Systems (DBMS) project demonstrating Oracle SQL and Flask integration.


## Oracle DCL Implementation

The system demonstrates comprehensive Oracle DCL features:

### User Creation
```sql
CREATE USER scm_admin IDENTIFIED BY Admin@123;
CREATE USER scm_manager IDENTIFIED BY Manager@123;
CREATE USER scm_warehouse IDENTIFIED BY Warehouse@123;
CREATE USER scm_viewer IDENTIFIED BY Viewer@123;
```

### Grant Permissions
```sql
-- Admin gets full access
GRANT CONNECT, RESOURCE TO scm_admin;

-- Manager gets selective permissions
GRANT SELECT, INSERT, UPDATE ON suppliers TO scm_manager;

-- Warehouse limited to inventory
GRANT SELECT, UPDATE ON inventory TO scm_warehouse;

-- Viewer read-only
GRANT SELECT ON all_tables TO scm_viewer;
```

### Revoke Permissions
```sql
REVOKE DELETE ON suppliers FROM scm_manager;
REVOKE INSERT ON products FROM scm_warehouse;
```

## SQL Features Demonstrated

- **DDL**: CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE INDEX, ALTER TABLE
- **DML**: INSERT, UPDATE, DELETE with constraints
- **DQL**: Complex SELECT with JOINs (INNER, LEFT, RIGHT)
- **DCL**: CREATE USER, GRANT, REVOKE permissions
- **TCL**: COMMIT, ROLLBACK, SAVEPOINT
- **Aggregates**: COUNT, SUM, AVG, MIN, MAX
- **Group By & Having**: Category and status analysis
- **Subqueries**: Nested SELECT for complex calculations
- **Views**: Reusable query abstractions
- **Indexes**: Performance optimization
- **Sequences**: Auto-increment primary keys
- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE

## Security Features

1. **Password Hashing**: All passwords stored as SHA-256 hashes
2. **Session Management**: Secure Flask sessions with secret key
3. **Role Validation**: Decorator-based permission checks on every route
4. **Audit Trail**: Complete log of all user actions with IP addresses
5. **Active Status**: Ability to deactivate users without deletion
6. **Protected Routes**: Login required for all operations

## Development

### Running in Debug Mode
```python
# app.py
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Environment Variables
- `DB_USER`: Oracle username (e.g., system)
- `DB_PASSWORD`: Oracle password
- `DB_DSN`: Database connection string (e.g., localhost:1521/XE)
- `SECRET_KEY`: Flask session secret (change in production!)
- `FLASK_ENV`: development or production

### Adding New Users
Login as admin and navigate to **Users** → **Add New User**

### Changing Passwords
```python
import hashlib
new_password = "your_new_password"
hashed = hashlib.sha256(new_password.encode()).hexdigest()
# Update in database: UPDATE app_users SET password = 'hash' WHERE username = 'user';
```

## Troubleshooting

### Database Connection Failed
1. Verify Oracle service is running:
   ```cmd
   net start OracleServiceXE
   ```
2. Check credentials in `.env`
3. Test connection:
   ```cmd
   sqlplus system/password@localhost:1521/XE
   ```

### Login Fails
- Verify `add_authentication.sql` was run
- Check default password hash matches
- Ensure `app_users` table exists

### Permission Denied
- Check user's role in database
- Verify session is active
- Try logging out and back in

### Import Errors
```cmd
setup.bat
```

### Tables Not Found
```sql
@schema.sql
@add_authentication.sql
```

## Production Deployment

### Security Checklist
- [ ] Change all default passwords
- [ ] Use strong `SECRET_KEY` in `.env`
- [ ] Enable HTTPS
- [ ] Implement password complexity requirements
- [ ] Add session timeouts
- [ ] Regular audit log reviews
- [ ] Backup database regularly
- [ ] Use environment-specific `.env` files

## API Routes

### Public
- `GET/POST /login` - User authentication

### Protected (Login Required)
- `GET /` - Dashboard
- `GET /suppliers` - View suppliers
- `POST /suppliers/add` - Add supplier (Admin, Manager)
- `POST /suppliers/delete/<id>` - Delete supplier (Admin only)
- `GET /inventory` - View inventory
- `POST /inventory/update/<id>` - Update stock (Admin, Manager, Warehouse)
- `GET /orders` - View orders
- `GET /analytics` - View reports

### Admin Only
- `GET /users` - View all users
- `GET/POST /users/add` - Create new user
- `POST /users/toggle/<id>` - Activate/deactivate user

## Testing

Test different roles to verify access control:

1. **Admin**: Full access, can delete records, manage users
2. **Manager**: Can add/edit but not delete
3. **Warehouse**: Only inventory operations
4. **Viewer**: Read-only everywhere

## License

This project is for educational purposes as a DBMS coursework demonstration.

## Author

Created by [jvkousthub](https://github.com/jvkousthub) - Database Management Systems project demonstrating Oracle SQL integration with Flask web application and enterprise-grade authentication.

## Screenshots

*Login page with role-based authentication*
*Dashboard with user information and role badge*
*User management interface (admin only)*
*Inventory management with permission-based actions*

---

**Star this repository if you found it helpful!**
