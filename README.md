# Supply Chain Management System with Real-Time Chat# Supply Chain Management System with Real-Time Chat# Supply Chain Management System with Real-Time Chat



A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, **real-time chat system**, and comprehensive **Oracle Database** integration.



---A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, **real-time chat system**, and comprehensive **Oracle Database** integration.A full-stack web application for managing supply chain operations with **role-based access control**, **user authentication**, **real-time chat system**, and comprehensive **Oracle Database** integration.



## 📑 Documentation Index



| Document | Description |------

|----------|-------------|

| **[README.md](README.md)** | Complete system documentation (this file) |

| **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)** | System architecture, database schema, and flow diagrams |

| **[schema.sql](schema.sql)** | Main database schema (DDL) |## 📑 Documentation Index## 📑 Documentation Index

| **[chat_schema.sql](chat_schema.sql)** | Chat system database schema with triggers |

| **[sample_data.sql](sample_data.sql)** | Sample data for testing (DML) |

| **[migrate_viewer_to_customer.sql](migrate_viewer_to_customer.sql)** | VIEWER→CUSTOMER role migration script |

| Document | Description |- **[README.md](README.md)** - This file: Complete system documentation

---

|----------|-------------|- **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)** - System architecture and flow diagrams

## 🌟 Features

| **[README.md](README.md)** | Complete system documentation (this file) |- **[schema.sql](schema.sql)** - Main database schema (DDL)

### Core Functionality

- **User Authentication**: Secure login with SHA-256 password hashing and session management| **[ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md)** | System architecture, database schema, and flow diagrams |- **[chat_schema.sql](chat_schema.sql)** - Chat system database schema

- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Customer)

- **Supplier Management**: Track and manage supplier information with ratings| **[schema.sql](schema.sql)** | Main database schema (DDL) |- **[sample_data.sql](sample_data.sql)** - Sample data for testing (DML)

- **Product Catalog**: Maintain product inventory with categories and pricing

- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking| **[chat_schema.sql](chat_schema.sql)** | Chat system database schema with triggers |- **[migrate_viewer_to_customer.sql](migrate_viewer_to_customer.sql)** - Role migration script

- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels

- **Order Processing**: Create and track purchase orders with status updates| **[sample_data.sql](sample_data.sql)** | Sample data for testing (DML) |

- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations

- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses| **[migrate_viewer_to_customer.sql](migrate_viewer_to_customer.sql)** | VIEWER→CUSTOMER role migration script |---



### 💬 Real-Time Chat System

- **Instant Messaging**: WebSocket-based real-time communication using Flask-SocketIO

- **Role-Based Messaging**: Hierarchical messaging based on user roles---## 🌟 Features

- **Broadcast Messages**: Admins/Managers can send to all users or specific roles

- **Automatic Notifications**: Database triggers for low stock alerts and order updates

- **Message Types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts

- **Priority Levels**: Low, Normal, High, Urgent (with visual indicators)## 🌟 Features### Core Functionality

- **Read Receipts**: Track message read status

- **Typing Indicators**: See when users are typing- **User Authentication**: Secure login with SHA-256 password hashing and session management

- **Desktop Notifications**: Browser-based notifications for new messages

- **Message Filtering**: Filter by all, unread, or alerts### Core Functionality- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Customer)

- **Modern UI**: Beautiful gradient design with smooth animations

- **User Authentication**: Secure login with SHA-256 password hashing and session management- **Supplier Management**: Track and manage supplier information with ratings

### Database Features

- **DDL**: Table creation with constraints, foreign keys, and indexes- **Role-Based Access Control**: 4 user roles with granular permissions (Admin, Manager, Warehouse, Customer)- **Product Catalog**: Maintain product inventory with categories and pricing

- **DML**: Insert, Update, Delete operations with data validation

- **DQL**: Complex SELECT queries with multi-table joins- **Supplier Management**: Track and manage supplier information with ratings- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking

- **DCL**: User permissions and role-based access control (GRANT, REVOKE)

- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)- **Product Catalog**: Maintain product inventory with categories and pricing- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels

- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views

- **Triggers**: Automatic message generation for business events (low stock, order updates)- **Warehouse Operations**: Manage multiple warehouse locations with capacity tracking- **Order Processing**: Create and track purchase orders with status updates



---- **Inventory Tracking**: Real-time stock monitoring with low-stock alerts and reorder levels- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations



## 🛠️ Tech Stack- **Order Processing**: Create and track purchase orders with status updates- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses



- **Backend**: Python 3.8+, Flask 3.0.0, Flask-SocketIO 5.3.6- **Analytics Dashboard**: Visualize data with advanced SQL queries and aggregations

- **Real-Time**: Socket.IO, gevent 25.5.1 (WebSocket support for Python 3.12+)

- **Database**: Oracle Database 11g or higher- **Audit Logging**: Complete audit trail tracking all user actions with timestamps and IP addresses### 💬 Real-Time Chat System

- **Driver**: python-oracledb (pure Python implementation - no Oracle client needed!)

- **Frontend**: HTML5, CSS3 with professional gradient theme, Jinja2 templates, Socket.IO Client- **Instant Messaging**: WebSocket-based real-time communication using Flask-SocketIO

- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection

### 💬 Real-Time Chat System- **Role-Based Messaging**: Hierarchical messaging based on user roles

---

- **Instant Messaging**: WebSocket-based real-time communication using Flask-SocketIO- **Broadcast Messages**: Admins/Managers can send to all users or specific roles

## 📦 Installation

- **Role-Based Messaging**: Hierarchical messaging based on user roles- **Automatic Notifications**: Database triggers for low stock alerts and order updates

### Prerequisites

- **Broadcast Messages**: Admins/Managers can send to all users or specific roles- **Message Types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))

- **Oracle Database** - XE 11g/18c/21c recommended ([Download Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html))- **Automatic Notifications**: Database triggers for low stock alerts and order updates- **Priority Levels**: Low, Normal, High, Urgent (with visual indicators)

- **Git** ([Download](https://git-scm.com/downloads))

- **Message Types**: General, Announcements, System Alerts, Order Updates, Low Stock Alerts- **Read Receipts**: Track message read status

### Quick Setup (5 Steps)

- **Priority Levels**: Low, Normal, High, Urgent (with visual indicators)- **Typing Indicators**: See when users are typing

#### Step 1: Clone Repository

```bash- **Read Receipts**: Track message read status- **Desktop Notifications**: Browser-based notifications for new messages

git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git

cd "Supply Chain Management DBMS"- **Typing Indicators**: See when users are typing- **Message Filtering**: Filter by all, unread, or alerts

```

- **Desktop Notifications**: Browser-based notifications for new messages- **Modern UI**: Beautiful gradient design with smooth animations

#### Step 2: Run Setup Script

```cmd- **Message Filtering**: Filter by all, unread, or alerts

setup.bat

```- **Modern UI**: Beautiful gradient design with smooth animations### Database Features

This will:

- Create Python virtual environment- **DDL**: Table creation with constraints, foreign keys, and indexes

- Install all dependencies (Flask, Flask-SocketIO, gevent, oracledb)

- Create `.env` configuration file### Database Features- **DML**: Insert, Update, Delete operations with data validation



#### Step 3: Configure Database Connection- **DDL**: Table creation with constraints, foreign keys, and indexes- **DQL**: Complex SELECT queries with multi-table joins



Edit `.env` file with your Oracle credentials:- **DML**: Insert, Update, Delete operations with data validation- **DCL**: User permissions and role-based access control (GRANT, REVOKE)

```properties

DB_USER=system- **DQL**: Complex SELECT queries with multi-table joins- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)

DB_PASSWORD=your_oracle_password

DB_DSN=localhost:1521/XE- **DCL**: User permissions and role-based access control (GRANT, REVOKE)- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views

SECRET_KEY=change-this-to-random-secret-key

```- **TCL**: Transaction management (COMMIT, ROLLBACK, SAVEPOINT)- **Triggers**: Automatic message generation for business events (low stock, order updates)



#### Step 4: Initialize Database- **Advanced SQL**: Aggregates, GROUP BY, HAVING, nested subqueries, materialized views



Connect to Oracle and run setup scripts:- **Triggers**: Automatic message generation for business events (low stock, order updates)## 🛠️ Tech Stack

```sql

sqlplus system/your_password@localhost:1521/XE



SQL> @schema.sql---- **Backend**: Python 3.8+, Flask 3.0.0, Flask-SocketIO 5.3.6

SQL> @sample_data.sql

SQL> @add_authentication.sql- **Real-Time**: Socket.IO, Eventlet (WebSocket support)

SQL> @chat_schema.sql

SQL> @migrate_viewer_to_customer.sql## 🛠️ Tech Stack- **Database**: Oracle Database 11g or higher

SQL> exit

```- **Driver**: python-oracledb (pure Python implementation)



#### Step 5: Start Application- **Backend**: Python 3.8+, Flask 3.0.0, Flask-SocketIO 5.3.6- **Frontend**: HTML5, CSS3 with professional navy blue theme, Jinja2 templates, Socket.IO Client

```cmd

run.bat- **Real-Time**: Socket.IO, gevent 25.5.1 (WebSocket support for Python 3.12+)- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection

```

- **Database**: Oracle Database 11g or higher

**Access the application**: Open browser at `http://localhost:5000`

- **Driver**: python-oracledb (pure Python implementation)## 📦 Installation

### Default Login Credentials

- **Frontend**: HTML5, CSS3 with professional gradient theme, Jinja2 templates, Socket.IO Client

| Username | Password | Role | Permissions |

|----------|----------|------|-------------|- **Security**: SHA-256 password hashing, session-based authentication, CSRF protection### Prerequisites

| **admin** | password123 | ADMIN | Full system access |

| **manager** | password123 | MANAGER | Add/Edit (no delete) |

| **warehouse** | password123 | WAREHOUSE | Inventory only |

| **customer** | password123 | CUSTOMER | Read-only access |---- Python 3.8 or higher



---- Oracle Database (XE 11g/18c/21c recommended)



## 👥 User Roles & Permissions## 📦 Installation- Git



### Role Hierarchy



#### 1. **ADMIN** (Highest Authority) 👑### Prerequisites### Setup Steps

- ✅ **Full system access** including user management

- ✅ Can **add, edit, and delete** all records

- ✅ Access to **audit logs**

- ✅ Can **broadcast messages to everyone**- Python 3.8 or higher1. **Clone the repository**

- 🎯 **Suitable for**: System administrators

- Oracle Database (XE 11g/18c/21c recommended)   ```bash

#### 2. **MANAGER** (Middle Management) 📊

- ✅ Can **view all data**- Git   git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git

- ✅ Can **add and edit** products, suppliers, orders

- ✅ Can **broadcast to WAREHOUSE and CUSTOMER** roles   cd "Supply Chain Management DBMS"

- ❌ **Cannot delete** records or manage users

- ✅ Access to **analytics and reports**### Quick Setup   ```

- 🎯 **Suitable for**: Supply chain managers, operations managers



#### 3. **WAREHOUSE** (Operations Staff) 📦

- ✅ Can **view and update inventory** quantities only1. **Clone the repository**2. **Run setup script**

- ✅ Limited to **inventory management**

- ✅ Can **receive messages** from ADMIN and MANAGER   ```bash   ```cmd

- ❌ **Cannot add products** or modify other data

- 🎯 **Suitable for**: Warehouse operators, stock keepers   git clone https://github.com/jvkousthub/Supply-Chain-Management-DBMS.git   setup.bat



#### 4. **CUSTOMER** (External Users) 👀   cd "Supply Chain Management DBMS"   ```

- ✅ **Read-only access** to all data

- ✅ Can **receive messages** from ADMIN and MANAGER   ```   This installs all dependencies and creates virtual environment.

- ❌ **Cannot add, edit, or delete** anything

- 🎯 **Suitable for**: External customers, vendors, auditors, partners



### Permissions Matrix2. **Run setup script**3. **Configure database**



| Permission | ADMIN | MANAGER | WAREHOUSE | CUSTOMER |   ```cmd   

|-----------|-------|---------|-----------|----------|

| 👁️ View Data | ✅ | ✅ | ✅ | ✅ |   setup.bat   Edit `.env` file with your Oracle credentials:

| ➕ Add Records | ✅ | ✅ | ❌ | ❌ |

| ✏️ Edit Records | ✅ | ✅ | ✅* | ❌ |   ```   ```properties

| 🗑️ Delete Records | ✅ | ❌ | ❌ | ❌ |

| 👥 Manage Users | ✅ | ❌ | ❌ | ❌ |   This installs all dependencies including Flask-SocketIO and gevent.   DB_USER=system

| 📋 View Audit Logs | ✅ | ❌ | ❌ | ❌ |

| 📢 Broadcast Messages | All | W+C | ❌ | ❌ |   DB_PASSWORD=your_password



*WAREHOUSE can only edit inventory levels3. **Configure database**   DB_DSN=localhost:1521/XE



### Chat System Hierarchy      SECRET_KEY=your-secret-key-here



```   Create/edit `.env` file with your Oracle credentials:   ```

ADMIN (Top Authority)

  ├── Can message: Everyone   ```properties

  └── Can broadcast: All users, specific roles, or individuals

   DB_USER=system4. **Run SQL scripts**

MANAGER

  ├── Can message: WAREHOUSE, CUSTOMER, other MANAGERs   DB_PASSWORD=your_password   

  └── Can broadcast: WAREHOUSE staff, CUSTOMERs

   DB_DSN=localhost:1521/XE   Connect to Oracle as system user:

WAREHOUSE

  ├── Can message: ADMIN, MANAGER   SECRET_KEY=your-secret-key-here   ```sql

  └── Cannot broadcast

   ```   sqlplus system/your_password@localhost:1521/XE

CUSTOMER

  ├── Can message: ADMIN, MANAGER   

  └── Cannot broadcast

```4. **Initialize database**   SQL> @schema.sql



---      SQL> @sample_data.sql



## 📂 Project Structure   Connect to Oracle and run setup scripts:   SQL> @add_authentication.sql



```   ```sql   SQL> exit

Supply Chain Management DBMS/

│   sqlplus system/your_password@localhost:1521/XE   ```

├── 📄 Core Application Files

│   ├── app.py                      # Flask app with Socket.IO integration   

│   ├── auth.py                     # Authentication and role decorators

│   ├── database.py                 # Database operations and queries   SQL> @schema.sql5. **Setup Chat System (NEW!)**

│   ├── chat_manager.py             # Chat business logic

│   └── requirements.txt            # Python dependencies   SQL> @sample_data.sql   ```cmd

│

├── 🗄️ Database Files   SQL> @add_authentication.sql   install_chat.bat

│   ├── schema.sql                  # Main database schema (DDL)

│   ├── chat_schema.sql             # Chat system schema with triggers   SQL> @chat_schema.sql   ```

│   ├── sample_data.sql             # Sample data (DML)

│   ├── add_authentication.sql      # User authentication setup   SQL> @migrate_viewer_to_customer.sql   

│   ├── user_roles_dcl.sql          # Oracle DCL implementation

│   ├── dcl_permissions.sql         # Additional permissions   SQL> exit   Then run in SQL:

│   ├── tcl_examples.sql            # Transaction examples (TCL)

│   ├── advanced_queries.sql        # Complex queries   ```   ```sql

│   ├── test_chat_system.sql        # Chat system verification

│   ├── chat_examples.sql           # Chat usage examples   SQL> @chat_schema.sql

│   └── migrate_viewer_to_customer.sql  # Role migration script

│5. **Start the application**   SQL> exit

├── 🎨 Templates

│   ├── base.html                   # Base template with navigation   ```cmd   ```

│   ├── login.html                  # Login page

│   ├── index.html                  # Dashboard   run.bat

│   ├── chat.html                   # Chat interface (1120+ lines)

│   ├── users.html                  # User management   ```6. **Start the application**

│   ├── suppliers.html              # Supplier management

│   ├── products.html               # Product catalog      ```cmd

│   ├── inventory.html              # Inventory tracking

│   ├── orders.html                 # Order management   Or manually:   run.bat

│   ├── analytics.html              # Analytics dashboard

│   └── ...                         # Other templates   ```cmd   ```

│

├── 📚 Documentation   python app.py   

│   ├── README.md                   # This file

│   └── ARCHITECTURE_DIAGRAMS.md    # System architecture diagrams   ```   Or manually:

│

└── 🔧 Configuration & Scripts   ```cmd

    ├── .env                        # Environment variables

    ├── .env.example                # Environment template6. **Access the application**   python app.py

    ├── .gitignore                  # Git ignore rules

    ├── setup.bat                   # Installation script      ```

    ├── run.bat                     # Start script

    └── install_chat.bat            # Chat dependencies installer   Open browser: `http://localhost:5000`

```

   7. **Open browser and login**

---

   **Default Login Credentials:**   

## 💬 Chat System

   | Username | Password | Role |   Navigate to: `http://localhost:5000`

### Features Overview

   |----------|----------|------|   

#### 1. **Real-time Messaging** ⚡

- 💬 Instant message delivery using WebSockets (Flask-SocketIO)   | admin | password123 | ADMIN |   **Default credentials:**

- 👥 Direct 1-on-1 conversations

- 📢 Broadcast messages to multiple users   | manager | password123 | MANAGER |   - Admin: `admin` / `password123`

- ✍️ Typing indicators

- ✅ Read receipts   | warehouse | password123 | WAREHOUSE |   - Manager: `manager` / `password123`

- 🔔 Desktop notifications (browser-based)

   | customer | password123 | CUSTOMER |   - Warehouse: `warehouse` / `password123`

#### 2. **Role-Based Access Control** 🔐

   - Viewer: `viewer` / `password123`

| Role | Can Send To | Broadcast Capability |

|------|-------------|---------------------|---

| **ADMIN** | Everyone | ✅ All users, specific roles, or individuals |

| **MANAGER** | Warehouse, Customer, Managers | ✅ Warehouse staff, customers |## 👥 User Roles & Permissions

| **WAREHOUSE** | Admin, Managers | ❌ No broadcast |

| **CUSTOMER** | Admin, Managers | ❌ No broadcast |## 👥 User Roles & Permissions



#### 3. **Automatic Notifications** 🤖| Role          | View All | Add Items | Edit Items | Delete Items | Update Inventory | Manage Users | Chat Access |



Database triggers automatically send messages for business events:### Role Hierarchy|------         |----------|-----------|------------|--------------|------------------|--------------|-------------|



**Low Stock Alerts:**| **ADMIN**     | Yes      | Yes       | Yes        | Yes          | Yes              | Yes          | Broadcast to All |

```sql

-- Automatically triggered when inventory <= reorder_level#### 1. **ADMIN** (Highest Authority)| **MANAGER**   | Yes      | Yes       | Yes        | No           | Yes              | No           | Broadcast to Staff |

UPDATE inventory SET quantity = 5 WHERE inventory_id = 1;

-- If quantity <= reorder_level, alert sent to all Admins & Managers- **Full system access** including user management| **WAREHOUSE** | Yes      | No        | No*        | No           | Yes*             | No           | Message Admins |

```

- Can **add, edit, and delete** all records| **VIEWER**    | Yes      | No        | No         | No           | No               | No           | Message Admins |

**Order Status Updates:**

```sql- Access to **audit logs**

-- Automatically triggered on order status change

UPDATE orders SET status = 'SHIPPED' WHERE order_id = 123;- Can **broadcast messages to everyone***WAREHOUSE role can only edit/update inventory quantities, nothing else.

-- Notification sent to Admins & Managers

```- **Suitable for**: System administrators



#### 4. **Message Types & Priorities** 🎨### Role Descriptions



**Message Types:**#### 2. **MANAGER** (Middle Management)

- 📝 **GENERAL** - Regular chat messages

- ⚠️ **LOW_STOCK_ALERT** - Automatic inventory alerts- Can **view all data**- **ADMIN**: Complete system control including user management, all CRUD operations, audit log access, and broadcast messaging to all users

- 📦 **ORDER_UPDATE** - Order status notifications

- 🚚 **DELIVERY_NOTICE** - Delivery updates- Can **add and edit** products, suppliers, orders- **MANAGER**: Can view all data and perform most operations except deletions and user management. Can broadcast to warehouse staff

- 🔴 **SYSTEM_ALERT** - System-wide alerts

- 📣 **ANNOUNCEMENT** - Important announcements- Can **broadcast to WAREHOUSE and CUSTOMER** roles- **WAREHOUSE**: Specialized role limited to viewing and updating inventory stock levels only. Can message admins/managers



**Priority Levels:**- **Cannot delete** records or manage users- **VIEWER**: Read-only access across all sections for reporting and analysis purposes. Can message admins/managers

- 🔵 **LOW** - Regular messages

- ⚪ **NORMAL** - Standard priority- Access to **analytics and reports**

- 🟠 **HIGH** - Important (orange border)

- 🔴 **URGENT** - Critical (red border with pulse animation)- **Suitable for**: Supply chain managers, operations managers### Chat Role Hierarchy



### Database Schema



The chat system uses **3 main tables**:#### 3. **WAREHOUSE** (Operations Staff)```



1. **`messages`**: Stores all messages with content, type, priority, broadcast flag- Can **view and update inventory** quantities onlyADMIN (Top Authority)

2. **`message_recipients`**: Tracks who receives each message and read status

3. **`chat_rooms`**: For future group chat functionality- Limited to **inventory management**  ├── Can message: Everyone



**Views:**- Can **receive messages** from ADMIN and MANAGER  └── Can broadcast: All users, specific roles, or individuals

- `user_inbox`: Messages for a specific user

- `message_details`: Complete message information with sender/recipient details- **Cannot add products** or modify other data

- `user_unread_count`: Count of unread messages per user

- **Suitable for**: Warehouse operators, stock keepersMANAGER

**Triggers:**

- `trg_low_stock_alert`: Automatically sends alerts when inventory ≤ reorder level  ├── Can message: WAREHOUSE, VIEWER, other MANAGERs

- `trg_order_status_notification`: Sends notifications on order status changes

#### 4. **CUSTOMER** (External Users/Read-Only)  └── Can broadcast: WAREHOUSE staff, VIEWERs

**Indexes for Performance:**

- Message sender/recipient lookups- **Read-only access** to all data

- Timestamp-based queries

- Read status filtering- Can **receive messages** from ADMIN and MANAGERWAREHOUSE



### Chat API Routes- **Cannot add, edit, or delete** anything  ├── Can message: ADMIN, MANAGER



**REST API:**- **Suitable for**: External customers, vendors, auditors, partners  └── Cannot broadcast

- `GET /chat` - Main chat interface

- `GET /api/messages` - Get user messages

- `POST /api/messages/send` - Send message

- `POST /api/messages/<id>/read` - Mark message as read### Permissions MatrixVIEWER

- `POST /api/messages/read-all` - Mark all messages as read

- `GET /api/users/role/<role>` - Get users by role  ├── Can message: ADMIN, MANAGER

- `GET /api/conversation/<user_id>` - Get conversation with specific user

| Permission            | ADMIN | MANAGER | WAREHOUSE | CUSTOMER |  └── Cannot broadcast

**Socket.IO Events:**

- `connect` / `disconnect` - Connection management|-----------------------|-------|---------|-----------|----------|```

- `send_message` - Real-time message sending

- `new_message` - Receive new messages| View Data             | ✅    | ✅      | ✅        | ✅       |

- `mark_read` - Mark message as read

- `typing` - Typing indicator| Add Records           | ✅    | ✅      | ❌        | ❌       |### Security Features

- `user_typing` - Receive typing notifications

| Edit Records          | ✅    | ✅      | ✅*       | ❌       |

### Usage Guide

| Delete Records        | ✅    | ❌      | ❌        | ❌       |- **Password Security**: SHA-256 hashing for all passwords

#### Sending Direct Messages:

1. Login to the system| Manage Users          | ✅    | ❌      | ❌        | ❌       |- **Session Management**: Secure session-based authentication

2. Click on **💬 Chat** in the navigation bar

3. Select a user from the left sidebar| View Audit Logs       | ✅    | ❌      | ❌        | ❌       |- **Access Control**: Route-level permission enforcement with decorators

4. Type your message in the input field

5. Press **Enter** or click "**Send**"| Broadcast Messages    | All   | W+C     | ❌        | ❌       |- **Audit Trail**: Complete logging of all user actions (login, logout, create, update, delete)



#### Broadcasting Messages (Admin/Manager only):- **UI Protection**: Dynamic button hiding based on user permissions

1. Click **"📢 Broadcast"** button in chat interface

2. Select target audience:*WAREHOUSE can only edit inventory levels- **IP Tracking**: Records IP addresses for all actions

   - **All Users**

   - **Specific Role** (MANAGER, WAREHOUSE, CUSTOMER)

   - **Custom user selection**

3. Choose **message type** and **priority level**### Chat System Hierarchy## Project Structure

4. Type message and send



#### Message Filtering:

- **All**: View all messages``````

- **Unread**: View only unread messages

- **Alerts**: View only system alerts and notificationsADMIN (Top Authority)├── app.py                      # Flask application with authentication routes



---  ├── Can message: Everyone├── auth.py                     # Authentication manager and role decorators



## 🗄️ Database Implementation  └── Can broadcast: All users, specific roles, or individuals├── database.py                 # Database operations and queries



### Schema Overview├── requirements.txt            # Python dependencies



**Main Tables (9):**MANAGER├── schema.sql                  # Database schema (DDL)

1. `suppliers` - Supplier information with ratings

2. `warehouses` - Warehouse locations and capacity  ├── Can message: WAREHOUSE, CUSTOMER, other MANAGERs├── sample_data.sql             # Sample data (DML)

3. `products` - Product catalog with categories

4. `inventory` - Stock levels with reorder points  └── Can broadcast: WAREHOUSE staff, CUSTOMERs├── add_authentication.sql      # User authentication setup

5. `orders` - Purchase orders with status tracking

6. `order_details` - Order line items├── user_roles_dcl.sql          # Oracle DCL implementation

7. `shipments` - Delivery tracking

8. `app_users` - User accounts with rolesWAREHOUSE├── dcl_permissions.sql         # Additional permissions (DCL)

9. `audit_log` - Action tracking with timestamps

  ├── Can message: ADMIN, MANAGER├── tcl_examples.sql            # Transaction examples (TCL)

**Chat Tables (3):**

10. `messages` - All chat messages  └── Cannot broadcast├── advanced_queries.sql        # Complex queries and analytics

11. `message_recipients` - Message delivery tracking

12. `chat_rooms` - Group chat rooms (for future use)



### Views (6)CUSTOMER├── templates/                  # HTML templates- View low-stock alerts



- `low_stock_items` - Products below reorder level  ├── Can message: ADMIN, MANAGER

- `order_summary` - Order aggregates by status

- `supplier_performance` - Supplier ratings and order counts  └── Cannot broadcast│   ├── base.html              # Base template with navbar- Update quantities

- `user_inbox` - User's messages

- `message_details` - Complete message info```

- `user_unread_count` - Unread message count

│   ├── login.html             # Login page- Track last updated timestamps

### Sequences (12)

---

Auto-increment IDs for all tables:

- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq`│   ├── users.html             # User management (admin)

- `order_seq`, `detail_seq`, `shipment_seq`

- `user_seq`, `log_seq`## 📂 Project Structure

- `message_seq`, `recipient_seq`, `room_seq`

│   ├── index.html             # Dashboard### Order Processing

### SQL Features Demonstrated

```

| Feature | Description | Example |

|---------|-------------|---------|Supply Chain Management DBMS/│   └── ...                    # Other templates- Create new orders

| **DDL** | CREATE TABLE, VIEW, SEQUENCE, INDEX, ALTER | Table creation with constraints |

| **DML** | INSERT, UPDATE, DELETE | Data manipulation with validation |│

| **DQL** | SELECT with JOINs | Complex multi-table queries |

| **DCL** | GRANT, REVOKE | User permissions |├── 📄 Core Application Files├── .env                        # Environment variables (create this)- Add products to orders

| **TCL** | COMMIT, ROLLBACK, SAVEPOINT | Transaction management |

| **Aggregates** | COUNT, SUM, AVG, MIN, MAX | Statistical analysis |│   ├── app.py                      # Flask app with Socket.IO integration

| **GROUP BY** | HAVING clause | Category-wise analysis |

| **Subqueries** | Nested SELECT | Complex calculations |│   ├── auth.py                     # Authentication and role decorators├── .gitignore                  # Git ignore rules- Update order status (PENDING → CONFIRMED → SHIPPED → DELIVERED)

| **Triggers** | Automatic actions | Low stock alerts, order notifications |

| **Constraints** | PK, FK, CHECK, UNIQUE | Data integrity |│   ├── database.py                 # Database operations and queries



---│   ├── chat_manager.py             # Chat business logic├── setup.bat                   # Installation script- View order details and history



## 🚀 Application Usage│   └── requirements.txt            # Python dependencies



### Dashboard Features│└── run.bat                     # Start script

- **User Information**: Display logged-in user with role badge

- **Quick Stats**: Total suppliers, products, warehouses, orders├── 🗄️ Database Files

- **Recent Activity**: Latest 5 orders with status

- **Low Stock Alerts**: Products needing reorder│   ├── schema.sql                  # Main database schema (DDL)```### Analytics

- **Chat Notifications**: Unread message count with badge

│   ├── chat_schema.sql             # Chat system schema with triggers

### Module-wise Capabilities

│   ├── sample_data.sql             # Sample data (DML)- Inventory by category (GROUP BY)

#### 👥 User Management (Admin Only)

- ➕ Create new users with role assignment│   ├── add_authentication.sql      # User authentication setup

- ✏️ Edit user details

- 🔄 Activate/Deactivate users│   ├── user_roles_dcl.sql          # Oracle DCL implementation## Database Schema- Top suppliers by order value (aggregates)

- 📊 View last login timestamps

- 🔍 Search and filter users│   ├── dcl_permissions.sql         # Additional permissions



#### 🏪 Supplier Management│   ├── tcl_examples.sql            # Transaction examples (TCL)- Warehouse utilization (subqueries)

- 📋 View all suppliers with ratings (1-5 stars)

- ➕ Add new suppliers with contact info│   ├── advanced_queries.sql        # Complex queries

- ✏️ Update supplier details (Admin, Manager)

- 🗑️ Delete suppliers (Admin only)│   └── migrate_viewer_to_customer.sql  # Role migration script### Main Tables- Products needing reorder (HAVING clause)

- 📈 Performance tracking

│

#### 📦 Product Catalog

- 📋 Browse products by category├── 🎨 Templates1. **suppliers** - Supplier information with ratings

- ➕ Add new products with pricing

- ✏️ Update product information│   ├── base.html                   # Base template with navigation

- 🗑️ Remove products (Admin only)

- 🔍 Search products│   ├── login.html                  # Login page2. **warehouses** - Warehouse locations and capacity## SQL Features Demonstrated



#### 🏭 Warehouse Operations│   ├── index.html                  # Dashboard

- 📍 Manage multiple warehouse locations

- 📊 Track capacity utilization│   ├── chat.html                   # Chat interface (1120+ lines)3. **products** - Product catalog with categories

- ➕ Add new warehouses

- ✏️ Update warehouse details│   ├── users.html                  # User management

- 📈 Inventory distribution

│   ├── suppliers.html              # Supplier management4. **inventory** - Stock levels with reorder points- **Joins**: INNER, LEFT, RIGHT

#### 📊 Inventory Management

- 👁️ Monitor stock levels across warehouses│   ├── products.html               # Product catalog

- ⚠️ View low-stock alerts (quantity ≤ reorder level)

- ✏️ Update quantities (Admin, Manager, Warehouse)│   ├── inventory.html              # Inventory tracking5. **orders** - Purchase orders with status tracking- **Aggregates**: COUNT, SUM, AVG, MIN, MAX

- 📅 Track last updated timestamps

- 🔔 Automatic notifications via chat│   ├── orders.html                 # Order management



#### 🛒 Order Processing│   ├── analytics.html              # Analytics dashboard6. **order_details** - Order line items- **Group By & Having**: Category analysis

- ➕ Create new purchase orders

- 📦 Add products to orders│   └── ...                         # Other templates

- 🔄 Update order status:

  - PENDING → CONFIRMED → SHIPPED → DELIVERED│7. **shipments** - Delivery tracking- **Subqueries**: Nested SELECT statements

- 📋 View complete order details

- 📜 Order history tracking├── 📚 Documentation

- 🔔 Status change notifications

│   ├── README.md                   # This file8. **app_users** - User accounts with roles- **Views**: Reusable query abstractions

#### 📈 Analytics Dashboard

- 📊 Inventory by category (GROUP BY)│   └── ARCHITECTURE_DIAGRAMS.md    # System architecture diagrams

- 🏆 Top suppliers by order value (aggregates)

- 🏭 Warehouse utilization (subqueries)│9. **audit_log** - Action tracking with timestamps- **Indexes**: Performance optimization

- ⚠️ Products needing reorder (HAVING clause)

- 📉 Order statistics by status└── 🔧 Configuration

- 💰 Revenue analysis

    ├── .env                        # Environment variables- **Sequences**: Auto-increment IDs

---

    ├── .gitignore                  # Git ignore rules

## 🔒 Security Features

    ├── setup.bat                   # Installation script### Views- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK

### Authentication & Authorization

1. **Password Hashing**: All passwords stored as SHA-256 hashes (never plain text)    └── run.bat                     # Start script

2. **Session Management**: Secure Flask sessions with secret key

3. **Role Validation**: Decorator-based permission checks on every route```- **low_stock_items** - Products below reorder level

4. **Login Required**: All routes protected except login page



### Audit & Monitoring

5. **Audit Trail**: Complete log of all user actions with:---- **order_summary** - Order aggregates by status## Development

   - Username and user ID

   - Action performed (CREATE, UPDATE, DELETE, LOGIN, LOGOUT)

   - Affected table name

   - Affected record ID## 💬 Chat System- **supplier_performance** - Supplier ratings and order counts

   - Timestamp (accurate to seconds)

   - IP address of the user

6. **Active Status**: Deactivate users without deletion (soft delete)

### Features### Running in Debug Mode

### Data Protection

7. **XSS Protection**: Template escaping with Jinja2

8. **CSRF Protection**: Session-based CSRF tokens

9. **Input Validation**: Server-side validation for all inputs#### 1. **Real-time Messaging**### SequencesFlask debug mode is enabled by default in `app.py`:

10. **SQL Injection Prevention**: Parameterized queries with oracledb

- ⚡ Instant message delivery using WebSockets (Flask-SocketIO)

---

- 💬 Direct 1-on-1 conversations- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq````python

## 🧪 Testing Guide

- 📢 Broadcast messages to multiple users

### Test Role-Based Access Control

- ✍️ Typing indicators- `order_seq`, `detail_seq`, `shipment_seq`app.run(debug=True, port=5000)

Login with different accounts to verify permissions:

- ✅ Read receipts

1. **Admin Test** (`admin/password123`):

   - ✅ Can access all modules- 🔔 Desktop notifications (browser-based)- `user_seq`, `log_seq````

   - ✅ Can delete records

   - ✅ Can manage users

   - ✅ Can broadcast to everyone

   - ✅ Can view audit logs#### 2. **Role-Based Access Control**



2. **Manager Test** (`manager/password123`):

   - ✅ Can view all data

   - ✅ Can add/edit products, suppliers, orders| Role | Can Send To | Broadcast |## Usage### Environment Variables

   - ✅ Can broadcast to WAREHOUSE and CUSTOMER

   - ❌ Cannot delete records|------|-------------|-----------|

   - ❌ Cannot manage users

| **ADMIN** | Everyone | ✅ All users, specific roles, or individuals |- `DB_USER`: Oracle username

3. **Warehouse Test** (`warehouse/password123`):

   - ✅ Can view inventory| **MANAGER** | Warehouse, Customer, Managers | ✅ Warehouse staff, customers |

   - ✅ Can update stock quantities

   - ✅ Can message admins/managers| **WAREHOUSE** | Admin, Managers | ❌ No broadcast |### Authentication- `DB_PASSWORD`: Oracle password

   - ❌ Cannot add products

   - ❌ Cannot broadcast| **CUSTOMER** | Admin, Managers | ❌ No broadcast |



4. **Customer Test** (`customer/password123`):- All routes require login (except `/login`)- `DB_DSN`: Database connection string

   - ✅ Can view all data (read-only)

   - ✅ Can receive messages#### 3. **Automatic Notifications** 🤖

   - ❌ Cannot modify anything

   - ❌ Cannot broadcast- Sessions persist until logout- `SECRET_KEY`: Flask session secret



### Test Chat SystemDatabase triggers automatically send messages for:



1. **Verify Database Setup**:- Automatic last login tracking- `FLASK_ENV`: development/production

```sql

-- Check tables exist**Low Stock Alerts:**

SELECT table_name FROM user_tables WHERE table_name LIKE '%MESSAGE%';

```sql

-- Check views

SELECT view_name FROM user_views;-- Automatically triggered when inventory <= reorder_level



-- Check triggersUPDATE inventory SET quantity = 5 WHERE inventory_id = 1;### Managing Users (Admin Only)## Troubleshooting

SELECT trigger_name FROM user_triggers WHERE trigger_name LIKE '%TRG%';

```-- If reorder_level >= 5, alert sent to all Admins & Managers



2. **Test Real-Time Messaging**:```- Create new users with assigned roles

   - Open two browsers (or incognito + normal)

   - Login as different users

   - Send messages and verify instant delivery

   - Check typing indicators work**Order Status Updates:**- Activate/deactivate user accounts### Database Connection Failed

   - Verify read receipts update

```sql

3. **Test Broadcast**:

   - Login as Admin-- Automatically triggered on order status change- View user activity and last login1. Verify Oracle service is running

   - Click "📢 Broadcast"

   - Select "All Users"UPDATE orders SET status = 'SHIPPED' WHERE order_id = 123;

   - Send message

   - Verify all users receive it-- Notification sent to Admins & Managers2. Check credentials in `.env`



4. **Test Automatic Notifications**:```

```sql

-- Trigger low stock alert### Managing Suppliers3. Test connection with SQL*Plus:

UPDATE inventory SET quantity = 3 WHERE product_id = 1;

-- Check if admins/managers received alert in chat#### 4. **Message Types & Priorities**



-- Trigger order notification- View all suppliers with ratings   ```

UPDATE orders SET status = 'SHIPPED' WHERE order_id = 1;

-- Check if admins/managers received notification**Message Types:**

```

- 📝 GENERAL - Regular messages- Add new suppliers with contact information   sqlplus username/password@localhost:1521/XEPDB1

---

- ⚠️ LOW_STOCK_ALERT - Inventory alerts

## 🐛 Troubleshooting

- 📦 ORDER_UPDATE - Order notifications- Update supplier details   ```

### Database Connection Issues

- 🚚 DELIVERY_NOTICE - Delivery updates

**Problem**: "Database connection failed"

- 🔴 SYSTEM_ALERT - System-wide alerts- Delete suppliers (Admin only)

**Solution**:

1. Verify Oracle service is running:- 📣 ANNOUNCEMENT - Important announcements

   ```cmd

   net start OracleServiceXE### Import Errors

   ```

2. Check credentials in `.env` file**Priority Levels:**

3. Test connection with SQL*Plus:

   ```cmd- 🔵 LOW - Regular messages### Inventory ManagementRun setup again:

   sqlplus system/password@localhost:1521/XE

   ```- ⚪ NORMAL - Standard priority

4. Verify DSN format: `localhost:1521/XE` (or `XEPDB1` for newer versions)

- 🟠 HIGH - Important (orange border)- Monitor stock levels across all warehouses```cmd

### Login Issues

- 🔴 URGENT - Critical (red border with pulse animation)

**Problem**: "Invalid username or password"

- View low-stock alertssetup.bat

**Solutions**:

- Verify `add_authentication.sql` was executed### Database Schema

- Check default credentials:

  ```sql- Update quantities (Admin, Manager, Warehouse)```

  SELECT username, role FROM app_users;

  ```The chat system uses 3 main tables:

- Ensure `app_users` table exists and has data

- Clear browser cookies and try again- Track last updated timestamps



### Permission Denied1. **`messages`**: Stores all messages with content, type, priority, broadcast flag



**Problem**: "You don't have permission to perform this action"2. **`message_recipients`**: Tracks who receives each message and read status### Tables Not Found



**Solutions**:3. **`chat_rooms`**: For future group chat functionality

- Check user's role in database:

  ```sql### Order ProcessingRun the schema creation:

  SELECT username, role, is_active FROM app_users WHERE username = 'your_username';

  ```**Views:**

- Verify user is active (`is_active = 1`)

- Logout and login again- `user_inbox`: Messages for a specific user- Create new orders with delivery dates```sql

- Check if session expired

- `message_details`: Complete message information with sender/recipient details

### Chat Not Working

- `user_unread_count`: Count of unread messages per user- Add products to orders@schema.sql

**Problem**: Chat messages not delivering in real-time



**Solutions**:

1. Verify dependencies are installed:**Triggers:**- Update order status: PENDING → CONFIRMED → SHIPPED → DELIVERED```

   ```cmd

   pip list | findstr socketio- `trg_low_stock_alert`: Automatically sends alerts when inventory ≤ reorder level

   pip list | findstr gevent

   ```- `trg_order_status_notification`: Sends notifications on order status changes- View complete order details and history

2. Check chat schema exists:

   ```sql

   SELECT table_name FROM user_tables WHERE table_name LIKE 'MESSAGE%';

   ```**Indexes for Performance:**## License

3. Check browser console for WebSocket errors (F12)

4. Ensure firewall allows port 5000- Message sender/recipient lookups

5. Try hard refresh (Ctrl+Shift+R)

- Timestamp-based queries### Analytics

### Import Errors

- Read status filtering

**Problem**: "ModuleNotFoundError: No module named 'flask_socketio'"

- Inventory by category (GROUP BY)This project is for educational purposes.

**Solution**:

```cmd### Chat API Routes

# Reinstall all dependencies

setup.bat- Top suppliers by order value (aggregates)



# Or manually:**REST API:**

pip install -r requirements.txt

```- `GET /chat` - Main chat interface- Warehouse utilization (subqueries)## Author



### Tables Not Found- `GET /api/messages` - Get user messages



**Problem**: "ORA-00942: table or view does not exist"- `POST /api/messages/send` - Send message- Products needing reorder (HAVING clause)



**Solution**:- `POST /api/messages/<id>/read` - Mark message as read

```sql

-- Run setup scripts in order- `POST /api/messages/read-all` - Mark all messages as read- Order statistics by statusCreated as a Database Management Systems (DBMS) project demonstrating Oracle SQL and Flask integration.

@schema.sql

@add_authentication.sql- `GET /api/users/role/<role>` - Get users by role

@chat_schema.sql

- `GET /api/conversation/<user_id>` - Get conversation with specific user

-- Verify tables exist

SELECT table_name FROM user_tables;## Oracle DCL Implementation

```

**Socket.IO Events:**

### Gevent Issues (Python 3.12+)

- `connect` / `disconnect` - Connection managementThe system demonstrates comprehensive Oracle DCL features:

**Problem**: "eventlet doesn't support Python 3.12"

- `send_message` - Real-time message sending

**Solution**:

Already fixed! Using `gevent` instead of `eventlet` in `requirements.txt`- `new_message` - Receive new messages### User Creation

```cmd

pip uninstall eventlet -y- `mark_read` - Mark message as read```sql

pip install gevent==25.5.1

```- `typing` - Typing indicatorCREATE USER scm_admin IDENTIFIED BY Admin@123;



---- `user_typing` - Receive typing notificationsCREATE USER scm_manager IDENTIFIED BY Manager@123;



## 🚀 Production Deployment ChecklistCREATE USER scm_warehouse IDENTIFIED BY Warehouse@123;



### Security### Usage GuideCREATE USER scm_viewer IDENTIFIED BY Viewer@123;



- [ ] Change all default passwords```

- [ ] Generate strong `SECRET_KEY` (256-bit random):

  ```python#### Sending Direct Messages:

  import secrets

  print(secrets.token_hex(32))1. Login to the system### Grant Permissions

  ```

- [ ] Set `FLASK_ENV=production` in `.env`2. Click on 💬 **Chat** in the navigation bar```sql

- [ ] Enable HTTPS with SSL certificate

- [ ] Implement password complexity requirements3. Select a user from the left sidebar-- Admin gets full access

- [ ] Add session timeouts (default: unlimited)

- [ ] Configure rate limiting for API endpoints4. Type your message in the input fieldGRANT CONNECT, RESOURCE TO scm_admin;

- [ ] Disable Flask debug mode (`debug=False` in `app.py`)

- [ ] Review and restrict DCL permissions5. Press Enter or click "Send"



### Database-- Manager gets selective permissions



- [ ] Create production database user (not system)#### Broadcasting Messages (Admin/Manager only):GRANT SELECT, INSERT, UPDATE ON suppliers TO scm_manager;

- [ ] Set up regular database backups

- [ ] Configure connection pooling1. Click **"📢 Broadcast"** button in chat interface

- [ ] Optimize indexes for production data volume

- [ ] Review and archive audit logs regularly2. Select target audience:-- Warehouse limited to inventory



### Server Configuration   - All UsersGRANT SELECT, UPDATE ON inventory TO scm_warehouse;



- [ ] Use production WSGI server (gunicorn/waitress):   - Specific Role (MANAGER, WAREHOUSE, CUSTOMER)

  ```cmd

  pip install waitress   - Custom user selection-- Viewer read-only

  waitress-serve --port=5000 app:app

  ```3. Choose message type and priority levelGRANT SELECT ON all_tables TO scm_viewer;

- [ ] Set up reverse proxy (nginx/Apache)

- [ ] Configure firewall rules4. Type message and send```

- [ ] Enable application logging

- [ ] Set up monitoring and alerts



### Environment Variables (Production)#### Message Filtering:### Revoke Permissions



```properties- **All**: View all messages```sql

# .env (PRODUCTION)

FLASK_ENV=production- **Unread**: View only unread messagesREVOKE DELETE ON suppliers FROM scm_manager;

DB_USER=scm_prod_user

DB_PASSWORD=<strong-secure-password>- **Alerts**: View only system alerts and notificationsREVOKE INSERT ON products FROM scm_warehouse;

DB_DSN=<production-db-host>:1521/ORCL

SECRET_KEY=<generated-256-bit-key>```

SESSION_TIMEOUT=3600

MAX_CONTENT_LENGTH=16777216---

```

## SQL Features Demonstrated

---

## 🗄️ Database Features

## 📄 License

- **DDL**: CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE INDEX, ALTER TABLE

This project is developed for **educational purposes** as a **Database Management Systems (DBMS) coursework demonstration**.

### Schema Overview- **DML**: INSERT, UPDATE, DELETE with constraints

Feel free to use this project for learning, but please provide attribution if you use it in your own projects.

- **DQL**: Complex SELECT with JOINs (INNER, LEFT, RIGHT)

---

**Main Tables:**- **DCL**: CREATE USER, GRANT, REVOKE permissions

## 👨‍💻 Author

1. `suppliers` - Supplier information with ratings- **TCL**: COMMIT, ROLLBACK, SAVEPOINT

**Created by**: [jvkousthub](https://github.com/jvkousthub)

2. `warehouses` - Warehouse locations and capacity- **Aggregates**: COUNT, SUM, AVG, MIN, MAX

**Project Type**: Database Management Systems (DBMS) Academic Project

3. `products` - Product catalog with categories- **Group By & Having**: Category and status analysis

**Demonstrates**:

- ✅ Oracle SQL integration with Python Flask4. `inventory` - Stock levels with reorder points- **Subqueries**: Nested SELECT for complex calculations

- ✅ Complete DBMS features (DDL, DML, DQL, DCL, TCL)

- ✅ Enterprise-grade authentication and authorization5. `orders` - Purchase orders with status tracking- **Views**: Reusable query abstractions

- ✅ Real-time WebSocket communication (Socket.IO)

- ✅ Role-based access control with 4-tier hierarchy6. `order_details` - Order line items- **Indexes**: Performance optimization

- ✅ Database triggers for automatic notifications

- ✅ Modern web application architecture7. `shipments` - Delivery tracking- **Sequences**: Auto-increment primary keys



---8. `app_users` - User accounts with roles- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE



## 📸 Application Screenshots9. `audit_log` - Action tracking with timestamps



### Login Page## Security Features

- Role-based authentication

- Default credentials for testing**Chat Tables:**

- Secure password hashing

10. `messages` - All chat messages1. **Password Hashing**: All passwords stored as SHA-256 hashes

### Dashboard

- User information with role badge11. `message_recipients` - Message delivery tracking2. **Session Management**: Secure Flask sessions with secret key

- Quick statistics

- Recent orders12. `chat_rooms` - Group chat rooms3. **Role Validation**: Decorator-based permission checks on every route

- Low stock alerts

- Unread message notifications4. **Audit Trail**: Complete log of all user actions with IP addresses



### User Management (Admin)### Views5. **Active Status**: Ability to deactivate users without deletion

- Create/edit/deactivate users

- Role assignment6. **Protected Routes**: Login required for all operations

- Last login tracking

- `low_stock_items` - Products below reorder level

### Inventory Management

- Stock level monitoring- `order_summary` - Order aggregates by status## Development

- Low stock alerts

- Update quantities (role-based)- `supplier_performance` - Supplier ratings and order counts

- Warehouse distribution

- `user_inbox` - User's messages### Running in Debug Mode

### Real-Time Chat

- 3-column layout (users, chat, messages)- `message_details` - Complete message info```python

- Direct messaging

- Broadcast capabilities- `user_unread_count` - Unread message count# app.py

- Message filtering

- Typing indicatorsif __name__ == '__main__':

- Read receipts

- Priority-based visual indicators### Sequences    app.run(debug=True, port=5000)



### Analytics Dashboard```

- Inventory by category charts

- Supplier performance metricsAuto-increment IDs for all tables:

- Warehouse utilization

- Order statistics- `supplier_seq`, `product_seq`, `warehouse_seq`, `inventory_seq`### Environment Variables



---- `order_seq`, `detail_seq`, `shipment_seq`- `DB_USER`: Oracle username (e.g., system)



## ⭐ Key Project Highlights- `user_seq`, `log_seq`- `DB_PASSWORD`: Oracle password



### Technical Excellence- `message_seq`, `recipient_seq`, `room_seq`- `DB_DSN`: Database connection string (e.g., localhost:1521/XE)

✅ **Complete DBMS Implementation** - All SQL features (DDL, DML, DQL, DCL, TCL)  

✅ **Oracle Database** - Enterprise-grade RDBMS with 12 tables  - `SECRET_KEY`: Flask session secret (change in production!)

✅ **Python Flask** - Modern web framework with 15+ routes  

✅ **Real-Time Communication** - WebSocket-based chat with Socket.IO  ### SQL Features Demonstrated- `FLASK_ENV`: development or production

✅ **Role-Based Security** - 4-tier hierarchical access control  

✅ **Database Triggers** - Automatic business event notifications  

✅ **Comprehensive Documentation** - README, architecture diagrams, code comments  

- **DDL**: CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE INDEX, ALTER TABLE### Adding New Users

### Educational Value

📚 **Demonstrates Oracle SQL Mastery**:- **DML**: INSERT, UPDATE, DELETE with constraintsLogin as admin and navigate to **Users** → **Add New User**

- Complex joins (INNER, LEFT, RIGHT)

- Aggregation functions (COUNT, SUM, AVG, MIN, MAX)- **DQL**: Complex SELECT with JOINs (INNER, LEFT, RIGHT)

- Subqueries and nested SELECT

- Views for data abstraction- **DCL**: CREATE USER, GRANT, REVOKE permissions### Changing Passwords

- Triggers for automatic actions

- Sequences for auto-increment- **TCL**: COMMIT, ROLLBACK, SAVEPOINT```python

- Constraints (PK, FK, CHECK, UNIQUE)

- **Aggregates**: COUNT, SUM, AVG, MIN, MAXimport hashlib

📚 **Full-Stack Web Development**:

- MVC architecture pattern- **Group By & Having**: Category and status analysisnew_password = "your_new_password"

- RESTful API design

- WebSocket real-time communication- **Subqueries**: Nested SELECT for complex calculationshashed = hashlib.sha256(new_password.encode()).hexdigest()

- Session-based authentication

- Template rendering with Jinja2- **Triggers**: Automatic actions on data changes# Update in database: UPDATE app_users SET password = 'hash' WHERE username = 'user';

- Responsive CSS design

- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE```

📚 **Software Engineering Best Practices**:

- Clean code structure

- Comprehensive error handling

- Security-first approach---## Troubleshooting

- Audit logging

- Modular design

- Version control with Git

## 🚀 Usage### Database Connection Failed

---

1. Verify Oracle service is running:

## 🎓 Perfect for DBMS Project Presentation

### Authentication   ```cmd

This project is **ideal for academic presentations** because it demonstrates:

- All routes require login (except `/login`)   net start OracleServiceXE

### 1. Complete DBMS Coverage ✅

- **DDL**: 12 tables with proper constraints- Sessions persist until logout   ```

- **DML**: INSERT, UPDATE, DELETE operations

- **DQL**: 20+ complex SELECT queries- Automatic last login tracking2. Check credentials in `.env`

- **DCL**: User management with GRANT/REVOKE

- **TCL**: Transaction management with COMMIT/ROLLBACK- IP address logging for security3. Test connection:

- **Advanced**: Triggers, views, sequences, indexes

   ```cmd

### 2. Real-World Application 🌍

- Solves actual supply chain management problems### Managing Users (Admin Only)   sqlplus system/password@localhost:1521/XE

- Industry-standard tech stack (Oracle + Python)

- Production-ready features (auth, audit, security)- Create new users with assigned roles   ```

- Modern UI/UX with real-time updates

- Activate/deactivate user accounts

### 3. Comprehensive Documentation 📖

- Professional README with all details- View user activity and last login### Login Fails

- Architecture diagrams for visual explanation

- Code comments for understanding- Password reset capability- Verify `add_authentication.sql` was run

- Setup scripts for easy demonstration

- Test cases for verification- Check default password hash matches



### 4. Impressive Features 🚀### Managing Suppliers- Ensure `app_users` table exists

- **Real-time chat** - Shows WebSocket mastery

- **Automatic notifications** - Demonstrates trigger usage- View all suppliers with ratings

- **Role-based access** - Security implementation

- **Audit logging** - Compliance and tracking- Add new suppliers with contact information### Permission Denied

- **Analytics dashboard** - Data visualization

- Update supplier details- Check user's role in database

### 5. Easy to Demonstrate 🎯

- Quick setup with `setup.bat`- Delete suppliers (Admin only)- Verify session is active

- Sample data included

- Multiple user roles to showcase- Try logging out and back in

- Live real-time features

- Clear visual indicators### Inventory Management



---- Monitor stock levels across all warehouses### Import Errors



## 🤝 Contributing- View low-stock alerts```cmd



This is an academic project, but suggestions and improvements are welcome!- Update quantities (Admin, Manager, Warehouse)setup.bat



If you find this project helpful, please:- Track last updated timestamps```

- ⭐ **Star the repository**

- 🔀 **Fork for your own learning**

- 📢 **Share with classmates**

- 💬 **Provide feedback via Issues**### Order Processing### Tables Not Found



---- Create new orders with delivery dates```sql



## 📞 Support & Contact- Add products to orders@schema.sql



For questions or issues:- Update order status: PENDING → CONFIRMED → SHIPPED → DELIVERED@add_authentication.sql

- **GitHub Issues**: [Submit an issue](https://github.com/jvkousthub/Supply-Chain-Management-DBMS/issues)

- **Email**: Contact via GitHub profile- View complete order details and history```

- **Documentation**: Check ARCHITECTURE_DIAGRAMS.md for detailed diagrams



---

### Analytics Dashboard## Production Deployment

## 🔗 Quick Links

- Inventory by category (GROUP BY)

- **[View Architecture Diagrams](ARCHITECTURE_DIAGRAMS.md)** - System design and flow charts

- **[Database Schema](schema.sql)** - Main table definitions- Top suppliers by order value (aggregates)### Security Checklist

- **[Chat Schema](chat_schema.sql)** - Chat system tables and triggers

- **[Sample Data](sample_data.sql)** - Test data for demonstration- Warehouse utilization (subqueries)- [ ] Change all default passwords

- **[Migration Script](migrate_viewer_to_customer.sql)** - Role update SQL

- Products needing reorder (HAVING clause)- [ ] Use strong `SECRET_KEY` in `.env`

---

- Order statistics by status- [ ] Enable HTTPS

**⭐ If this project helped you with your DBMS course, please star the repository!**

- [ ] Implement password complexity requirements

**Built with ❤️ for Database Management Systems coursework**

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
