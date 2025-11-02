# Supply Chain Management System with Real-Time Chat# Supply Chain Management System with Real-Time Chat



A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, **real-time chat system**, and comprehensive **Oracle Database** integration.A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, **real-time chat system**, and comprehensive **Oracle Database** integration.



------



## 📑 Documentation Index## 📑 Documentation Index



| Document | Description |- **[README.md](README.md)** - This file: Complete system documentation

|----------|-------------|- **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)** - System architecture and flow diagrams

| **[README.md](README.md)** | Complete system documentation (this file) |- **[schema.sql](schema.sql)** - Main database schema (DDL)

| **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)** | System architecture, database schema, and flow diagrams |- **[chat_schema.sql](chat_schema.sql)** - Chat system database schema

| **[schema.sql](schema.sql)** | Main database schema (DDL) |- **[sample_data.sql](sample_data.sql)** - Sample data for testing (DML)

| **[chat_schema.sql](chat_schema.sql)** | Chat system database schema with triggers |- **[migrate_viewer_to_customer.sql](migrate_viewer_to_customer.sql)** - Role migration script

| **[sample_data.sql](sample_data.sql)** | Sample data for testing (DML) |

| **[migrate_viewer_to_customer.sql](migrate_viewer_to_customer.sql)** | VIEWER→CUSTOMER role migration script |---



---## 🌟 Features



## 🌟 Features### Core Functionality

- **User Authentication**: Secure login with SHA-256 password hashing and session management

### Core Functionality- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Customer)

- **User Authentication**: Secure login with SHA-256 password hashing and session management- **Supplier Management**: Track and manage supplier information with ratings

- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Customer)- **Product Catalog**: Maintain product inventory with categories and pricing

- **Supplier Management**: Track and manage supplier information with ratings- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking

- **Product Catalog**: Maintain product inventory with categories and pricing- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels

- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking- **Order Processing**: Create and track purchase orders with status updates

- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations

- **Order Processing**: Create and track purchase orders with status updates- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses

- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations

- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses### 💬 Real-Time Chat System

- **Instant Messaging**: WebSocket-based real-time communication using Flask-SocketIO

### 💬 Real-Time Chat System- **Role-Based Messaging**: Hierarchical messaging based on user roles

- **Instant Messaging**: WebSocket-based real-time communication using Flask-SocketIO- **Broadcast Messages**: Admins/Managers can send to all users or specific roles

- **Role-Based Messaging**: Hierarchical messaging based on user roles- **Automatic Notifications**: Database triggers for low stock alerts and order updates

- **Broadcast Messages**: Admins/Managers can send to all users or specific roles- **Message Types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts

- **Automatic Notifications**: Database triggers for low stock alerts and order updates- **Priority Levels**: Low, Normal, High, Urgent (with visual indicators)

- **Message Types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts- **Read Receipts**: Track message read status

- **Priority Levels**: Low, Normal, High, Urgent (with visual indicators)- **Typing Indicators**: See when users are typing

- **Read Receipts**: Track message read status- **Desktop Notifications**: Browser-based notifications for new messages

- **Typing Indicators**: See when users are typing- **Message Filtering**: Filter by all, unread, or alerts

- **Desktop Notifications**: Browser-based notifications for new messages- **Modern UI**: Beautiful gradient design with smooth animations

- **Message Filtering**: Filter by all, unread, or alerts

- **Modern UI**: Beautiful gradient design with smooth animations### Database Features

- **DDL**: Table creation with constraints, foreign keys, and indexes

### Database Features- **DML**: Insert, Update, Delete operations with data validation

- **DDL**: Table creation with constraints, foreign keys, and indexes- **DQL**: Complex SELECT queries with multi-table joins

- **DML**: Insert, Update, Delete operations with data validation- **DCL**: User permissions and role-based access control (GRANT, REVOKE)

- **DQL**: Complex SELECT queries with multi-table joins- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)

- **DCL**: User permissions and role-based access control (GRANT, REVOKE)- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views

- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)- **Triggers**: Automatic message generation for business events (low stock, order updates)

- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views

- **Triggers**: Automatic message generation for business events (low stock, order updates)## 🛠️ Tech Stack



---- **Backend**: Python 3.8+, Flask 3.0.0, Flask-SocketIO 5.3.6

- **Real-Time**: Socket.IO, Eventlet (WebSocket support)

## 🛠️ Tech Stack- **Database**: Oracle Database 11g or higher

- **Driver**: python-oracledb (pure Python implementation)

- **Backend**: Python 3.8+, Flask 3.0.0, Flask-SocketIO 5.3.6- **Frontend**: HTML5, CSS3 with professional navy blue theme, Jinja2 templates, Socket.IO Client

- **Real-Time**: Socket.IO, gevent 25.5.1 (WebSocket support for Python 3.12+)- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection

- **Database**: Oracle Database 11g or higher

- **Driver**: python-oracledb (pure Python implementation)## 📦 Installation

- **Frontend**: HTML5, CSS3 with professional gradient theme, Jinja2 templates, Socket.IO Client

- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection### Prerequisites



---- Python 3.8 or higher

- Oracle Database (XE 11g/18c/21c recommended)

## 📦 Installation- Git



### Prerequisites### Setup Steps



- Python 3.8 or higher1. **Clone the repository**

- Oracle Database (XE 11g/18c/21c recommended)   ```bash

- Git   git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git

   cd "Supply Chain Management DBMS"

### Quick Setup   ```



1. **Clone the repository**2. **Run setup script**

   ```bash   ```cmd

   git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git   setup.bat

   cd "Supply Chain Management DBMS"   ```

   ```   This installs all dependencies and creates virtual environment.



2. **Run setup script**3. **Configure database**

   ```cmd   

   setup.bat   Edit `.env` file with your Oracle credentials:

   ```   ```properties

   This installs all dependencies including Flask-SocketIO and gevent.   DB_USER=system

   DB_PASSWORD=your_password

3. **Configure database**   DB_DSN=localhost:1521/XE

      SECRET_KEY=your-secret-key-here

   Create/edit `.env` file with your Oracle credentials:   ```

   ```properties

   DB_USER=system4. **Run SQL scripts**

   DB_PASSWORD=your_password   

   DB_DSN=localhost:1521/XE   Connect to Oracle as system user:

   SECRET_KEY=your-secret-key-here   ```sql

   ```   sqlplus system/your_password@localhost:1521/XE

   

4. **Initialize database**   SQL> @schema.sql

      SQL> @sample_data.sql

   Connect to Oracle and run setup scripts:   SQL> @add_authentication.sql

   ```sql   SQL> exit

   sqlplus system/your_password@localhost:1521/XE   ```

   

   SQL> @schema.sql5. **Setup Chat System (NEW!)**

   SQL> @sample_data.sql   ```cmd

   SQL> @add_authentication.sql   install_chat.bat

   SQL> @chat_schema.sql   ```

   SQL> @migrate_viewer_to_customer.sql   

   SQL> exit   Then run in SQL:

   ```   ```sql

   SQL> @chat_schema.sql

5. **Start the application**   SQL> exit

   ```cmd   ```

   run.bat

   ```6. **Start the application**

      ```cmd

   Or manually:   run.bat

   ```cmd   ```

   python app.py   

   ```   Or manually:

   ```cmd

6. **Access the application**   python app.py

      ```

   Open browser: `http://localhost:5000`

   7. **Open browser and login**

   **Default Login Credentials:**   

   | Username | Password | Role |   Navigate to: `http://localhost:5000`

   |----------|----------|------|   

   | admin | password123 | ADMIN |   **Default credentials:**

   | manager | password123 | MANAGER |   - Admin: `admin` / `password123`

   | warehouse | password123 | WAREHOUSE |   - Manager: `manager` / `password123`

   | customer | password123 | CUSTOMER |   - Warehouse: `warehouse` / `password123`

   - Viewer: `viewer` / `password123`

---

## 👥 User Roles & Permissions

## 👥 User Roles & Permissions

| Role          | View All | Add Items | Edit Items | Delete Items | Update Inventory | Manage Users | Chat Access |

### Role Hierarchy|------         |----------|-----------|------------|--------------|------------------|--------------|-------------|

| **ADMIN**     | Yes      | Yes       | Yes        | Yes          | Yes              | Yes          | Broadcast to All |

#### 1. **ADMIN** (Highest Authority)| **MANAGER**   | Yes      | Yes       | Yes        | No           | Yes              | No           | Broadcast to Staff |

- **Full system access** including user management| **WAREHOUSE** | Yes      | No        | No*        | No           | Yes*             | No           | Message Admins |

- Can **add, edit, and delete** all records| **VIEWER**    | Yes      | No        | No         | No           | No               | No           | Message Admins |

- Access to **audit logs**

- Can **broadcast messages to everyone***WAREHOUSE role can only edit/update inventory quantities, nothing else.

- **Suitable for**: System administrators

### Role Descriptions

#### 2. **MANAGER** (Middle Management)

- Can **view all data**- **ADMIN**: Complete system control including user management, all CRUD operations, audit log access, and broadcast messaging to all users

- Can **add and edit** products, suppliers, orders- **MANAGER**: Can view all data and perform most operations except deletions and user management. Can broadcast to warehouse staff

- Can **broadcast to WAREHOUSE and CUSTOMER** roles- **WAREHOUSE**: Specialized role limited to viewing and updating inventory stock levels only. Can message admins/managers

- **Cannot delete** records or manage users- **VIEWER**: Read-only access across all sections for reporting and analysis purposes. Can message admins/managers

- Access to **analytics and reports**

- **Suitable for**: Supply chain managers, operations managers### Chat Role Hierarchy



#### 3. **WAREHOUSE** (Operations Staff)```

- Can **view and update inventory** quantities onlyADMIN (Top Authority)

- Limited to **inventory management**  ├── Can message: Everyone

- Can **receive messages** from ADMIN and MANAGER  └── Can broadcast: All users, specific roles, or individuals

- **Cannot add products** or modify other data

- **Suitable for**: Warehouse operators, stock keepersMANAGER

  ├── Can message: WAREHOUSE, VIEWER, other MANAGERs

#### 4. **CUSTOMER** (External Users/Read-Only)  └── Can broadcast: WAREHOUSE staff, VIEWERs

- **Read-only access** to all data

- Can **receive messages** from ADMIN and MANAGERWAREHOUSE

- **Cannot add, edit, or delete** anything  ├── Can message: ADMIN, MANAGER

- **Suitable for**: External customers, vendors, auditors, partners  └── Cannot broadcast



### Permissions MatrixVIEWER

  ├── Can message: ADMIN, MANAGER

| Permission            | ADMIN | MANAGER | WAREHOUSE | CUSTOMER |  └── Cannot broadcast

|-----------------------|-------|---------|-----------|----------|```

| View Data             | ✅    | ✅      | ✅        | ✅       |

| Add Records           | ✅    | ✅      | ❌        | ❌       |### Security Features

| Edit Records          | ✅    | ✅      | ✅*       | ❌       |

| Delete Records        | ✅    | ❌      | ❌        | ❌       |- **Password Security**: SHA-256 hashing for all passwords

| Manage Users          | ✅    | ❌      | ❌        | ❌       |- **Session Management**: Secure session-based authentication

| View Audit Logs       | ✅    | ❌      | ❌        | ❌       |- **Access Control**: Route-level permission enforcement with decorators

| Broadcast Messages    | All   | W+C     | ❌        | ❌       |- **Audit Trail**: Complete logging of all user actions (login, logout, create, update, delete)

- **UI Protection**: Dynamic button hiding based on user permissions

*WAREHOUSE can only edit inventory levels- **IP Tracking**: Records IP addresses for all actions



### Chat System Hierarchy## Project Structure



``````

ADMIN (Top Authority)├── app.py                      # Flask application with authentication routes

  ├── Can message: Everyone├── auth.py                     # Authentication manager and role decorators

  └── Can broadcast: All users, specific roles, or individuals├── database.py                 # Database operations and queries

├── requirements.txt            # Python dependencies

MANAGER├── schema.sql                  # Database schema (DDL)

  ├── Can message: WAREHOUSE, CUSTOMER, other MANAGERs├── sample_data.sql             # Sample data (DML)

  └── Can broadcast: WAREHOUSE staff, CUSTOMERs├── add_authentication.sql      # User authentication setup

├── user_roles_dcl.sql          # Oracle DCL implementation

WAREHOUSE├── dcl_permissions.sql         # Additional permissions (DCL)

  ├── Can message: ADMIN, MANAGER├── tcl_examples.sql            # Transaction examples (TCL)

  └── Cannot broadcast├── advanced_queries.sql        # Complex queries and analytics



CUSTOMER├── templates/                  # HTML templates- View low-stock alerts

  ├── Can message: ADMIN, MANAGER

  └── Cannot broadcast│   ├── base.html              # Base template with navbar- Update quantities

```

│   ├── login.html             # Login page- Track last updated timestamps

---

│   ├── users.html             # User management (admin)

## 📂 Project Structure

│   ├── index.html             # Dashboard### Order Processing

```

Supply Chain Management DBMS/│   └── ...                    # Other templates- Create new orders

│

├── 📄 Core Application Files├── .env                        # Environment variables (create this)- Add products to orders

│   ├── app.py                      # Flask app with Socket.IO integration

│   ├── auth.py                     # Authentication and role decorators├── .gitignore                  # Git ignore rules- Update order status (PENDING → CONFIRMED → SHIPPED → DELIVERED)

│   ├── database.py                 # Database operations and queries

│   ├── chat_manager.py             # Chat business logic├── setup.bat                   # Installation script- View order details and history

│   └── requirements.txt            # Python dependencies

│└── run.bat                     # Start script

├── 🗄️ Database Files

│   ├── schema.sql                  # Main database schema (DDL)```### Analytics

│   ├── chat_schema.sql             # Chat system schema with triggers

│   ├── sample_data.sql             # Sample data (DML)- Inventory by category (GROUP BY)

│   ├── add_authentication.sql      # User authentication setup

│   ├── user_roles_dcl.sql          # Oracle DCL implementation## Database Schema- Top suppliers by order value (aggregates)

│   ├── dcl_permissions.sql         # Additional permissions

│   ├── tcl_examples.sql            # Transaction examples (TCL)- Warehouse utilization (subqueries)

│   ├── advanced_queries.sql        # Complex queries

│   └── migrate_viewer_to_customer.sql  # Role migration script### Main Tables- Products needing reorder (HAVING clause)

│

├── 🎨 Templates1. **suppliers** - Supplier information with ratings

│   ├── base.html                   # Base template with navigation

│   ├── login.html                  # Login page2. **warehouses** - Warehouse locations and capacity## SQL Features Demonstrated

│   ├── index.html                  # Dashboard

│   ├── chat.html                   # Chat interface (1120+ lines)3. **products** - Product catalog with categories

│   ├── users.html                  # User management

│   ├── suppliers.html              # Supplier management4. **inventory** - Stock levels with reorder points- **Joins**: INNER, LEFT, RIGHT

│   ├── products.html               # Product catalog

│   ├── inventory.html              # Inventory tracking5. **orders** - Purchase orders with status tracking- **Aggregates**: COUNT, SUM, AVG, MIN, MAX

│   ├── orders.html                 # Order management

│   ├── analytics.html              # Analytics dashboard6. **order_details** - Order line items- **Group By & Having**: Category analysis

│   └── ...                         # Other templates

│7. **shipments** - Delivery tracking- **Subqueries**: Nested SELECT statements

├── 📚 Documentation

│   ├── README.md                   # This file8. **app_users** - User accounts with roles- **Views**: Reusable query abstractions

│   └── ARCHITECTURE_DIAGRAMS.md    # System architecture diagrams

│9. **audit_log** - Action tracking with timestamps- **Indexes**: Performance optimization

└── 🔧 Configuration

    ├── .env                        # Environment variables- **Sequences**: Auto-increment IDs

    ├── .gitignore                  # Git ignore rules

    ├── setup.bat                   # Installation script### Views- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK

    └── run.bat                     # Start script

```- **low_stock_items** - Products below reorder level



---- **order_summary** - Order aggregates by status## Development



## 💬 Chat System- **supplier_performance** - Supplier ratings and order counts



### Features### Running in Debug Mode



#### 1. **Real-time Messaging**### SequencesFlask debug mode is enabled by default in `app.py`:

- ⚡ Instant message delivery using WebSockets (Flask-SocketIO)

- 💬 Direct 1-on-1 conversations- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq````python

- 📢 Broadcast messages to multiple users

- ✍️ Typing indicators- `order_seq`, `detail_seq`, `shipment_seq`app.run(debug=True, port=5000)

- ✅ Read receipts

- 🔔 Desktop notifications (browser-based)- `user_seq`, `log_seq````



#### 2. **Role-Based Access Control**



| Role | Can Send To | Broadcast |## Usage### Environment Variables

|------|-------------|-----------|

| **ADMIN** | Everyone | ✅ All users, specific roles, or individuals |- `DB_USER`: Oracle username

| **MANAGER** | Warehouse, Customer, Managers | ✅ Warehouse staff, customers |

| **WAREHOUSE** | Admin, Managers | ❌ No broadcast |### Authentication- `DB_PASSWORD`: Oracle password

| **CUSTOMER** | Admin, Managers | ❌ No broadcast |

- All routes require login (except `/login`)- `DB_DSN`: Database connection string

#### 3. **Automatic Notifications** 🤖

- Sessions persist until logout- `SECRET_KEY`: Flask session secret

Database triggers automatically send messages for:

- Automatic last login tracking- `FLASK_ENV`: development/production

**Low Stock Alerts:**

```sql

-- Automatically triggered when inventory <= reorder_level

UPDATE inventory SET quantity = 5 WHERE inventory_id = 1;### Managing Users (Admin Only)## Troubleshooting

-- If reorder_level >= 5, alert sent to all Admins & Managers

```- Create new users with assigned roles



**Order Status Updates:**- Activate/deactivate user accounts### Database Connection Failed

```sql

-- Automatically triggered on order status change- View user activity and last login1. Verify Oracle service is running

UPDATE orders SET status = 'SHIPPED' WHERE order_id = 123;

-- Notification sent to Admins & Managers2. Check credentials in `.env`

```

### Managing Suppliers3. Test connection with SQL*Plus:

#### 4. **Message Types & Priorities**

- View all suppliers with ratings   ```

**Message Types:**

- 📝 GENERAL - Regular messages- Add new suppliers with contact information   sqlplus username/password@localhost:1521/XEPDB1

- ⚠️ LOW_STOCK_ALERT - Inventory alerts

- 📦 ORDER_UPDATE - Order notifications- Update supplier details   ```

- 🚚 DELIVERY_NOTICE - Delivery updates

- 🔴 SYSTEM_ALERT - System-wide alerts- Delete suppliers (Admin only)

- 📣 ANNOUNCEMENT - Important announcements

### Import Errors

**Priority Levels:**

- 🔵 LOW - Regular messages### Inventory ManagementRun setup again:

- ⚪ NORMAL - Standard priority

- 🟠 HIGH - Important (orange border)- Monitor stock levels across all warehouses```cmd

- 🔴 URGENT - Critical (red border with pulse animation)

- View low-stock alertssetup.bat

### Database Schema

- Update quantities (Admin, Manager, Warehouse)```

The chat system uses 3 main tables:

- Track last updated timestamps

1. **`messages`**: Stores all messages with content, type, priority, broadcast flag

2. **`message_recipients`**: Tracks who receives each message and read status### Tables Not Found

3. **`chat_rooms`**: For future group chat functionality

### Order ProcessingRun the schema creation:

**Views:**

- `user_inbox`: Messages for a specific user- Create new orders with delivery dates```sql

- `message_details`: Complete message information with sender/recipient details

- `user_unread_count`: Count of unread messages per user- Add products to orders@schema.sql



**Triggers:**- Update order status: PENDING → CONFIRMED → SHIPPED → DELIVERED```

- `trg_low_stock_alert`: Automatically sends alerts when inventory ≤ reorder level

- `trg_order_status_notification`: Sends notifications on order status changes- View complete order details and history



**Indexes for Performance:**## License

- Message sender/recipient lookups

- Timestamp-based queries### Analytics

- Read status filtering

- Inventory by category (GROUP BY)This project is for educational purposes.

### Chat API Routes

- Top suppliers by order value (aggregates)

**REST API:**

- `GET /chat` - Main chat interface- Warehouse utilization (subqueries)## Author

- `GET /api/messages` - Get user messages

- `POST /api/messages/send` - Send message- Products needing reorder (HAVING clause)

- `POST /api/messages/<id>/read` - Mark message as read

- `POST /api/messages/read-all` - Mark all messages as read- Order statistics by statusCreated as a Database Management Systems (DBMS) project demonstrating Oracle SQL and Flask integration.

- `GET /api/users/role/<role>` - Get users by role

- `GET /api/conversation/<user_id>` - Get conversation with specific user

## Oracle DCL Implementation

**Socket.IO Events:**

- `connect` / `disconnect` - Connection managementThe system demonstrates comprehensive Oracle DCL features:

- `send_message` - Real-time message sending

- `new_message` - Receive new messages### User Creation

- `mark_read` - Mark message as read```sql

- `typing` - Typing indicatorCREATE USER scm_admin IDENTIFIED BY Admin@123;

- `user_typing` - Receive typing notificationsCREATE USER scm_manager IDENTIFIED BY Manager@123;

CREATE USER scm_warehouse IDENTIFIED BY Warehouse@123;

### Usage GuideCREATE USER scm_viewer IDENTIFIED BY Viewer@123;

```

#### Sending Direct Messages:

1. Login to the system### Grant Permissions

2. Click on 💬 **Chat** in the navigation bar```sql

3. Select a user from the left sidebar-- Admin gets full access

4. Type your message in the input fieldGRANT CONNECT, RESOURCE TO scm_admin;

5. Press Enter or click "Send"

-- Manager gets selective permissions

#### Broadcasting Messages (Admin/Manager only):GRANT SELECT, INSERT, UPDATE ON suppliers TO scm_manager;

1. Click **"📢 Broadcast"** button in chat interface

2. Select target audience:-- Warehouse limited to inventory

   - All UsersGRANT SELECT, UPDATE ON inventory TO scm_warehouse;

   - Specific Role (MANAGER, WAREHOUSE, CUSTOMER)

   - Custom user selection-- Viewer read-only

3. Choose message type and priority levelGRANT SELECT ON all_tables TO scm_viewer;

4. Type message and send```



#### Message Filtering:### Revoke Permissions

- **All**: View all messages```sql

- **Unread**: View only unread messagesREVOKE DELETE ON suppliers FROM scm_manager;

- **Alerts**: View only system alerts and notificationsREVOKE INSERT ON products FROM scm_warehouse;

```

---

## SQL Features Demonstrated

## 🗄️ Database Features

- **DDL**: CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE INDEX, ALTER TABLE

### Schema Overview- **DML**: INSERT, UPDATE, DELETE with constraints

- **DQL**: Complex SELECT with JOINs (INNER, LEFT, RIGHT)

**Main Tables:**- **DCL**: CREATE USER, GRANT, REVOKE permissions

1. `suppliers` - Supplier information with ratings- **TCL**: COMMIT, ROLLBACK, SAVEPOINT

2. `warehouses` - Warehouse locations and capacity- **Aggregates**: COUNT, SUM, AVG, MIN, MAX

3. `products` - Product catalog with categories- **Group By & Having**: Category and status analysis

4. `inventory` - Stock levels with reorder points- **Subqueries**: Nested SELECT for complex calculations

5. `orders` - Purchase orders with status tracking- **Views**: Reusable query abstractions

6. `order_details` - Order line items- **Indexes**: Performance optimization

7. `shipments` - Delivery tracking- **Sequences**: Auto-increment primary keys

8. `app_users` - User accounts with roles- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE

9. `audit_log` - Action tracking with timestamps

## Security Features

**Chat Tables:**

10. `messages` - All chat messages1. **Password Hashing**: All passwords stored as SHA-256 hashes

11. `message_recipients` - Message delivery tracking2. **Session Management**: Secure Flask sessions with secret key

12. `chat_rooms` - Group chat rooms3. **Role Validation**: Decorator-based permission checks on every route

4. **Audit Trail**: Complete log of all user actions with IP addresses

### Views5. **Active Status**: Ability to deactivate users without deletion

6. **Protected Routes**: Login required for all operations

- `low_stock_items` - Products below reorder level

- `order_summary` - Order aggregates by status## Development

- `supplier_performance` - Supplier ratings and order counts

- `user_inbox` - User's messages### Running in Debug Mode

- `message_details` - Complete message info```python

- `user_unread_count` - Unread message count# app.py

if __name__ == '__main__':

### Sequences    app.run(debug=True, port=5000)

```

Auto-increment IDs for all tables:

- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq`### Environment Variables

- `order_seq`, `detail_seq`, `shipment_seq`- `DB_USER`: Oracle username (e.g., system)

- `user_seq`, `log_seq`- `DB_PASSWORD`: Oracle password

- `message_seq`, `recipient_seq`, `room_seq`- `DB_DSN`: Database connection string (e.g., localhost:1521/XE)

- `SECRET_KEY`: Flask session secret (change in production!)

### SQL Features Demonstrated- `FLASK_ENV`: development or production



- **DDL**: CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE INDEX, ALTER TABLE### Adding New Users

- **DML**: INSERT, UPDATE, DELETE with constraintsLogin as admin and navigate to **Users** → **Add New User**

- **DQL**: Complex SELECT with JOINs (INNER, LEFT, RIGHT)

- **DCL**: CREATE USER, GRANT, REVOKE permissions### Changing Passwords

- **TCL**: COMMIT, ROLLBACK, SAVEPOINT```python

- **Aggregates**: COUNT, SUM, AVG, MIN, MAXimport hashlib

- **Group By & Having**: Category and status analysisnew_password = "your_new_password"

- **Subqueries**: Nested SELECT for complex calculationshashed = hashlib.sha256(new_password.encode()).hexdigest()

- **Triggers**: Automatic actions on data changes# Update in database: UPDATE app_users SET password = 'hash' WHERE username = 'user';

- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE```



---## Troubleshooting



## 🚀 Usage### Database Connection Failed

1. Verify Oracle service is running:

### Authentication   ```cmd

- All routes require login (except `/login`)   net start OracleServiceXE

- Sessions persist until logout   ```

- Automatic last login tracking2. Check credentials in `.env`

- IP address logging for security3. Test connection:

   ```cmd

### Managing Users (Admin Only)   sqlplus system/password@localhost:1521/XE

- Create new users with assigned roles   ```

- Activate/deactivate user accounts

- View user activity and last login### Login Fails

- Password reset capability- Verify `add_authentication.sql` was run

- Check default password hash matches

### Managing Suppliers- Ensure `app_users` table exists

- View all suppliers with ratings

- Add new suppliers with contact information### Permission Denied

- Update supplier details- Check user's role in database

- Delete suppliers (Admin only)- Verify session is active

- Try logging out and back in

### Inventory Management

- Monitor stock levels across all warehouses### Import Errors

- View low-stock alerts```cmd

- Update quantities (Admin, Manager, Warehouse)setup.bat

- Track last updated timestamps```



### Order Processing### Tables Not Found

- Create new orders with delivery dates```sql

- Add products to orders@schema.sql

- Update order status: PENDING → CONFIRMED → SHIPPED → DELIVERED@add_authentication.sql

- View complete order details and history```



### Analytics Dashboard## Production Deployment

- Inventory by category (GROUP BY)

- Top suppliers by order value (aggregates)### Security Checklist

- Warehouse utilization (subqueries)- [ ] Change all default passwords

- Products needing reorder (HAVING clause)- [ ] Use strong `SECRET_KEY` in `.env`

- Order statistics by status- [ ] Enable HTTPS

- [ ] Implement password complexity requirements

---- [ ] Add session timeouts

- [ ] Regular audit log reviews

## 🔒 Security Features- [ ] Backup database regularly

- [ ] Use environment-specific `.env` files

1. **Password Hashing**: All passwords stored as SHA-256 hashes

2. **Session Management**: Secure Flask sessions with secret key## 💬 Chat System

3. **Role Validation**: Decorator-based permission checks on every route

4. **Audit Trail**: Complete log of all user actions with IP addresses and timestamps### Features

5. **Active Status**: Ability to deactivate users without deletion- **Real-time messaging** using WebSocket (Flask-SocketIO)

6. **Protected Routes**: Login required for all operations- **Role-based communication** with hierarchical permissions

7. **XSS Protection**: Template escaping with Jinja2- **Broadcast messaging** for admins and managers

8. **CSRF Protection**: Session-based CSRF tokens- **Automatic notifications** via database triggers

- **Message types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts

---- **Priority levels**: Low, Normal, High, Urgent (with visual indicators)

- **Read receipts** and **typing indicators**

## 🧪 Testing- **Desktop notifications** for new messages

- **Modern UI** with gradient design and smooth animations

### Test Different Roles

### Quick Start

Login with different accounts to verify access control:1. Install dependencies: `install_chat.bat`

2. Setup database: `@chat_schema.sql`

1. **Admin**: Full access, can delete records, manage users, broadcast to all3. Access chat: Click 💬 in navigation bar

2. **Manager**: Can add/edit but not delete, broadcast to staff

3. **Warehouse**: Only inventory operations, message admins### Chat Routes

4. **Customer**: Read-only everywhere, message admins- `GET /chat` - Main chat interface

- `GET /api/messages` - Get user messages

### Chat System Testing- `POST /api/messages/send` - Send message

- `POST /api/messages/<recipient_id>/read` - Mark as read

1. Run verification script in Oracle:- `POST /api/messages/read-all` - Mark all read

   ```sql- `GET /api/users/role/<role>` - Get users by role

   -- Verify chat schema setup- `GET /api/conversation/<user_id>` - Get conversation

   SELECT table_name FROM user_tables WHERE table_name LIKE '%MESSAGE%';

   SELECT view_name FROM user_views;### Socket.IO Events

   SELECT trigger_name FROM user_triggers;- `connect` / `disconnect` - Connection management

   ```- `send_message` - Real-time message sending

- `new_message` - Receive new messages

2. Test messaging:- `mark_read` - Mark message as read

   - Login as different users in multiple browsers- `typing` - Typing indicator

   - Send direct messages- `user_typing` - Receive typing notifications

   - Test broadcast functionality

   - Verify real-time delivery### Automatic Notifications

Database triggers automatically send messages for:

3. Test automatic notifications:- **Low Stock**: When inventory ≤ reorder level

   ```sql- **Order Updates**: When order status changes

   -- Trigger low stock alert

   UPDATE inventory SET quantity = 3 WHERE product_id = 1;### Documentation

   - `QUICK_START.txt` - Quick setup guide

   -- Trigger order notification- `CHAT_SETUP_README.md` - Detailed documentation

   UPDATE orders SET status = 'SHIPPED' WHERE order_id = 1;- `IMPLEMENTATION_SUMMARY.md` - Feature overview

   ```- `chat_examples.sql` - Usage examples

- `test_chat_system.sql` - Testing script

---

## 📡 API Routes

## 🐛 Troubleshooting

### Public

### Database Connection Failed- `GET/POST /login` - User authentication

1. Verify Oracle service is running:

   ```cmd### Protected (Login Required)

   net start OracleServiceXE- `GET /` - Dashboard

   ```- `GET /suppliers` - View suppliers

2. Check credentials in `.env` file- `POST /suppliers/add` - Add supplier (Admin, Manager)

3. Test connection with SQL*Plus:- `POST /suppliers/delete/<id>` - Delete supplier (Admin only)

   ```cmd- `GET /inventory` - View inventory

   sqlplus system/password@localhost:1521/XE- `POST /inventory/update/<id>` - Update stock (Admin, Manager, Warehouse)

   ```- `GET /orders` - View orders

- `GET /analytics` - View reports

### Login Fails- `GET /chat` - Chat interface (NEW!)

- Verify `add_authentication.sql` was executed

- Check default password hash matches### Admin Only

- Ensure `app_users` table exists and has data- `GET /users` - View all users

- Clear browser cache and cookies- `GET/POST /users/add` - Create new user

- `POST /users/toggle/<id>` - Activate/deactivate user

### Permission Denied

- Check user's role in database:## 🧪 Testing

  ```sql

  SELECT username, role FROM app_users;Test different roles to verify access control:

  ```

- Verify session is active1. **Admin**: Full access, can delete records, manage users, broadcast to all

- Try logging out and back in2. **Manager**: Can add/edit but not delete, broadcast to staff

3. **Warehouse**: Only inventory operations, message admins

### Chat Not Working4. **Viewer**: Read-only everywhere, message admins

- Verify Flask-SocketIO and gevent are installed:

  ```cmd### Chat System Testing

  pip list | findstr socketio1. Run `@test_chat_system.sql` to verify setup

  pip list | findstr gevent2. Login as different users in multiple browsers

  ```3. Send messages and verify real-time delivery

- Check chat schema is installed:4. Update inventory to trigger low stock alerts

  ```sql5. Change order status to trigger notifications

  SELECT table_name FROM user_tables WHERE table_name LIKE 'MESSAGE%';

  ```## 📄 License

- Check browser console for WebSocket errors

- Ensure firewall allows port 5000This project is for educational purposes as a DBMS coursework demonstration.



### Import Errors## 👨‍💻 Author

```cmd

# Reinstall dependenciesCreated by [jvkousthub](https://github.com/jvkousthub) - Database Management Systems project demonstrating Oracle SQL integration with Flask web application, enterprise-grade authentication, and real-time chat system.

setup.bat

```## 📸 Screenshots



### Tables Not Found*Login page with role-based authentication*

```sql*Dashboard with user information and role badge*

-- Run setup scripts*User management interface (admin only)*

@schema.sql*Inventory management with permission-based actions*

@add_authentication.sql*Real-time chat with broadcast messaging and automatic notifications*

@chat_schema.sql

```---



---**⭐ Star this repository if you found it helpful!**



## 🚀 Production Deployment### Key Highlights

✅ **Oracle SQL** - Complete DBMS integration  

### Security Checklist✅ **Flask** - Modern Python web framework  

- [ ] Change all default passwords✅ **Real-Time Chat** - WebSocket-based messaging  

- [ ] Use strong `SECRET_KEY` in `.env`✅ **Role-Based Access** - Hierarchical permissions  

- [ ] Enable HTTPS with SSL certificate✅ **Auto Notifications** - Database triggers  

- [ ] Implement password complexity requirements✅ **Production Ready** - Authentication, audit logs, security

- [ ] Add session timeouts (currently unlimited)
- [ ] Configure rate limiting for API endpoints
- [ ] Set up regular database backups
- [ ] Review audit logs regularly
- [ ] Use environment-specific `.env` files
- [ ] Disable Flask debug mode (`debug=False`)
- [ ] Configure production WSGI server (gunicorn/waitress)
- [ ] Set up reverse proxy (nginx/Apache)

### Recommended Environment Variables
```properties
FLASK_ENV=production
DB_USER=scm_production_user
DB_PASSWORD=<strong-password>
DB_DSN=<production-db-connection-string>
SECRET_KEY=<generate-random-256-bit-key>
SESSION_TIMEOUT=3600
```

---

## 📄 License

This project is for educational purposes as a Database Management Systems (DBMS) coursework demonstration.

---

## 👨‍💻 Author

Created by **[jvkousthub](https://github.com/jvkousthub)**

Database Management Systems project demonstrating:
- Oracle SQL integration with Python Flask
- Enterprise-grade authentication and authorization
- Real-time WebSocket communication
- Role-based access control
- Complete DBMS feature implementation (DDL, DML, DQL, DCL, TCL)

---

## 📸 Screenshots

*Login page with role-based authentication*
*Dashboard with user information and role badge*
*User management interface (admin only)*
*Inventory management with permission-based actions*
*Real-time chat with broadcast messaging and automatic notifications*

---

## ⭐ Key Highlights

✅ **Oracle SQL** - Complete DBMS integration with DDL, DML, DQL, DCL, TCL  
✅ **Flask** - Modern Python web framework with Jinja2 templates  
✅ **Real-Time Chat** - WebSocket-based messaging with Socket.IO  
✅ **Role-Based Access** - 4-tier hierarchical permission system  
✅ **Auto Notifications** - Database triggers for business events  
✅ **Production Ready** - Authentication, audit logs, security features  
✅ **Comprehensive Documentation** - Architecture diagrams, setup guides, API docs  

---

**⭐ Star this repository if you found it helpful!**

For detailed architecture and flow diagrams, see **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)**
