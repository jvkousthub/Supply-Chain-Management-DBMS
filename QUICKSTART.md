# 🚀 Quick Start Guide

## Get Running in 5 Minutes

### Step 1: Setup (One Time)
```cmd
setup.bat
```
This installs all dependencies and creates virtual environment.

### Step 2: Database Setup (One Time)
```cmd
sqlplus system/your_password@localhost:1521/XE

SQL> @schema.sql
SQL> @sample_data.sql
SQL> @add_authentication.sql
SQL> exit
```

### Step 3: Run the Application
```cmd
run.bat
```

### Step 4: Open Browser
Navigate to: **http://localhost:5000**

### Step 5: Login and Test

| Username | Password | Role | What You Can Do |
|----------|----------|------|-----------------|
| `admin` | `password123` | Admin | Everything including user management |
| `manager` | `password123` | Manager | View all, add/edit items, no delete |
| `warehouse` | `password123` | Warehouse | Only update inventory |
| `viewer` | `password123` | Viewer | View only, no changes |

## What to Test

### As ADMIN
1. ✅ Navigate to all pages - should see all buttons
2. ✅ Click "Users" in navbar - should work
3. ✅ Try deleting a supplier - should work
4. ✅ Update inventory - should work

### As MANAGER  
1. ✅ Navigate to suppliers - should NOT see Delete buttons
2. ✅ Try adding a product - should work
3. ✅ Try accessing /users URL directly - should be blocked
4. ✅ Update inventory - should work

### As WAREHOUSE
1. ✅ Navigate to inventory - should see update forms
2. ✅ Navigate to suppliers - should NOT see any buttons
3. ✅ Try accessing /products/add URL - should be blocked
4. ✅ Update inventory quantity - should work

### As VIEWER
1. ✅ Navigate to all pages - should see data but NO buttons
2. ✅ Try any action URL directly - should be blocked
3. ✅ Inventory page - should NOT see update forms

## Quick Troubleshooting

### Can't Connect to Database?
```cmd
# Check if Oracle is running
services.msc
# Look for OracleServiceXE - should be "Running"
```

### Login Not Working?
```sql
-- Check users exist
sqlplus system/password@localhost:1521/XE
SQL> SELECT username, role FROM app_users;
```

### Import Errors?
```cmd
setup.bat
```

## Common Credentials Issues

If you changed your Oracle password, update in both places:

**1. In setup.bat:**
```batch
set DB_USER=system
set DB_PASSWORD=your_actual_password
set DB_DSN=localhost:1521/XE
```

**2. Create .env file:**
```
DB_USER=system
DB_PASSWORD=your_actual_password
DB_DSN=localhost:1521/XE
SECRET_KEY=your-secret-key-change-this
```

## Success Indicators

✅ Terminal shows: `✓ Database connection successful!`
✅ Terminal shows: `Running on http://127.0.0.1:5000`
✅ Browser shows login page
✅ Can login with admin/password123
✅ See your name and role badge in top-right corner

## Need Help?

- **README.md** - Complete documentation
- **ROLE_TESTING_GUIDE.md** - Detailed testing procedures  
- **IMPLEMENTATION_SUMMARY.md** - Technical details

## Verify Everything Works

After logging in as admin:
1. Go to Users page
2. Look at audit_log entries
3. All your logins should be logged

Run this query to verify:
```sql
SELECT username, action, TO_CHAR(action_time, 'HH24:MI:SS')
FROM audit_log
ORDER BY log_id DESC
FETCH FIRST 10 ROWS ONLY;
```

---

**That's it! You're ready to demonstrate your Supply Chain Management System! 🎉**
