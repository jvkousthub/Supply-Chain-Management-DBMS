# Supply Chain Management System

A full-stack web application for managing supply chain operations using **Oracle Database** and **Flask**.

## Features

- **Supplier Management**: Track and manage supplier information
- **Product Catalog**: Maintain product inventory with categories
- **Warehouse Operations**: Manage multiple warehouse locations
- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts
- **Order Processing**: Create and track purchase orders
- **Analytics Dashboard**: Visualize data with advanced SQL queries

## Database Features

- **DDL**: Table creation with constraints and indexes
- **DML**: Insert, Update, Delete operations
- **DQL**: Complex SELECT queries with joins
- **DCL**: User permissions and access control
- **TCL**: Transaction management (COMMIT, ROLLBACK)
- **Advanced SQL**: Aggregates, GROUP BY, HAVING, subqueries, views

## Tech Stack

- **Backend**: Python 3.8+, Flask 3.0.0
- **Database**: Oracle Database 11g or higher
- **Driver**: python-oracledb (pure Python)
- **Frontend**: HTML5, CSS3, Jinja2

## Installation

### Prerequisites

- Python 3.8 or higher
- Oracle Database (XE 11g/18c/21c recommended)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Supply Chain Management DBMS"
   ```

2. **Run setup script**
   ```cmd
   setup.bat
   ```
   This will:
   - Create a virtual environment
   - Install all dependencies
   - Create a `.env` file template

3. **Configure database**
   
   Edit `.env` file with your Oracle credentials:
   ```properties
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_DSN=localhost:1521/XEPDB1
   SECRET_KEY=your-secret-key
   ```

4. **Create database schema**
   
   Connect to Oracle and run:
   ```sql
   @schema.sql
   @sample_data.sql
   ```

5. **Start the application**
   ```cmd
   run.bat
   ```

6. **Open browser**
   
   Navigate to: `http://localhost:5000`

## Project Structure

```
├── app.py                  # Flask application
├── database.py             # Database operations
├── requirements.txt        # Python dependencies
├── schema.sql             # Database schema (DDL)
├── sample_data.sql        # Sample data (DML)
├── dcl_permissions.sql    # User permissions (DCL)
├── tcl_examples.sql       # Transaction examples (TCL)
├── advanced_queries.sql   # Complex queries
├── templates/             # HTML templates
├── .env                   # Environment variables (create this)
├── setup.bat             # Installation script
└── run.bat               # Start script
```

## Database Schema

### Tables
1. **suppliers** - Supplier information
2. **warehouses** - Warehouse locations
3. **products** - Product catalog
4. **inventory** - Stock levels
5. **orders** - Purchase orders
6. **order_details** - Order line items
7. **shipments** - Delivery tracking

### Views
- **low_stock_items** - Products below reorder level
- **order_summary** - Order aggregates
- **supplier_performance** - Supplier ratings

## Usage

### Managing Suppliers
- View all suppliers
- Add new suppliers with ratings
- Update supplier information
- Delete suppliers

### Inventory Management
- Monitor stock levels across warehouses
- View low-stock alerts
- Update quantities
- Track last updated timestamps

### Order Processing
- Create new orders
- Add products to orders
- Update order status (PENDING → CONFIRMED → SHIPPED → DELIVERED)
- View order details and history

### Analytics
- Inventory by category (GROUP BY)
- Top suppliers by order value (aggregates)
- Warehouse utilization (subqueries)
- Products needing reorder (HAVING clause)

## SQL Features Demonstrated

- **Joins**: INNER, LEFT, RIGHT
- **Aggregates**: COUNT, SUM, AVG, MIN, MAX
- **Group By & Having**: Category analysis
- **Subqueries**: Nested SELECT statements
- **Views**: Reusable query abstractions
- **Indexes**: Performance optimization
- **Sequences**: Auto-increment IDs
- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK

## Development

### Running in Debug Mode
Flask debug mode is enabled by default in `app.py`:
```python
app.run(debug=True, port=5000)
```

### Environment Variables
- `DB_USER`: Oracle username
- `DB_PASSWORD`: Oracle password
- `DB_DSN`: Database connection string
- `SECRET_KEY`: Flask session secret
- `FLASK_ENV`: development/production

## Troubleshooting

### Database Connection Failed
1. Verify Oracle service is running
2. Check credentials in `.env`
3. Test connection with SQL*Plus:
   ```
   sqlplus username/password@localhost:1521/XEPDB1
   ```

### Import Errors
Run setup again:
```cmd
setup.bat
```

### Tables Not Found
Run the schema creation:
```sql
@schema.sql
```

## License

This project is for educational purposes.

## Author

Created as a Database Management Systems (DBMS) project demonstrating Oracle SQL and Flask integration.
