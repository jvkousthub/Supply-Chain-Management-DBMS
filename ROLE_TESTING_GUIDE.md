# Role-Based Access Control Testing Guide

## Overview
This guide helps you test the role-based access control implementation in the Supply Chain Management System.

## Default User Accounts
All accounts use password: `password123`

| Username | Role | Full Access Description |
|----------|------|------------------------|
| admin | ADMIN | Full system access - can view, add, edit, and delete everything |
| manager | MANAGER | Can view all, add/edit products, suppliers, warehouses, and orders, but cannot delete |
| warehouse | WAREHOUSE | Can only view and update inventory quantities |
| viewer | VIEWER | Read-only access to all sections |

## What to Test

### 1. ADMIN Role (username: admin)
**Expected Access:**
- ✅ View all sections (Suppliers, Products, Warehouses, Inventory, Orders, Analytics)
- ✅ See "Add" buttons on Suppliers, Products, Warehouses, Orders
- ✅ See "Edit" buttons on Suppliers
- ✅ See "Delete" buttons on Suppliers and Products
- ✅ Update inventory quantities
- ✅ Update order status
- ✅ Access Users management page

**Test Actions:**
1. Login as `admin` / `password123`
2. Navigate to Suppliers - should see "Add New Supplier", "Edit", and "Delete" buttons
3. Navigate to Products - should see "Add New Product" and "Delete" buttons
4. Navigate to Warehouses - should see "Add New Warehouse" button
5. Navigate to Inventory - should see update forms for quantities
6. Navigate to Orders - should see "Create New Order" button
7. Click on an order - should see status update form
8. Navigate to Users - should be accessible from navbar

### 2. MANAGER Role (username: manager)
**Expected Access:**
- ✅ View all sections
- ✅ See "Add" buttons on Suppliers, Products, Warehouses, Orders
- ✅ See "Edit" buttons on Suppliers
- ❌ No "Delete" buttons (not authorized)
- ✅ Update inventory quantities
- ✅ Update order status
- ❌ No Users management access

**Test Actions:**
1. Login as `manager` / `password123`
2. Navigate to Suppliers - should see "Add New Supplier" and "Edit" buttons, but NO "Delete" button
3. Navigate to Products - should see "Add New Product" but NO "Delete" button
4. Navigate to Warehouses - should see "Add New Warehouse" button
5. Navigate to Inventory - should see update forms
6. Navigate to Orders - should see "Create New Order" button
7. Click on an order - should see status update form
8. Check navbar - should NOT see "Users" link
9. Try accessing /users directly - should be denied with "Insufficient permissions"

### 3. WAREHOUSE Role (username: warehouse)
**Expected Access:**
- ✅ View Inventory and Low Stock sections
- ✅ Update inventory quantities ONLY
- ❌ No "Add" buttons anywhere
- ❌ No "Edit" buttons (except inventory)
- ❌ No "Delete" buttons
- ❌ Cannot create orders or update order status
- ❌ No Users management access

**Test Actions:**
1. Login as `warehouse` / `password123`
2. Navigate to Inventory - should see update forms for quantities
3. Navigate to Suppliers - should see list but NO action buttons
4. Navigate to Products - should see list but NO action buttons
5. Navigate to Warehouses - should see list but NO "Add" button
6. Navigate to Orders - should see list but NO "Create New Order" button
7. Click on an order - should see order details but NO status update form
8. Try accessing /suppliers/add directly - should be denied with "Insufficient permissions"

### 4. VIEWER Role (username: viewer)
**Expected Access:**
- ✅ View all sections (read-only)
- ❌ No "Add" buttons
- ❌ No "Edit" buttons
- ❌ No "Delete" buttons
- ❌ No inventory update forms
- ❌ No order creation or status updates
- ❌ No Users management access

**Test Actions:**
1. Login as `viewer` / `password123`
2. Navigate to all sections - should see data but absolutely NO action buttons
3. Navigate to Inventory - should see quantities but NO update forms
4. Navigate to Orders - should see list but NO "Create New Order" button
5. Click on an order - should see details but NO status update form
6. Try accessing /products/add directly - should be denied with "Insufficient permissions"

## Common Issues to Check

### Issue 1: Action Buttons Still Visible
**Symptom:** User sees buttons they shouldn't have access to
**Fix:** Check that permissions are properly passed to templates via context processor

### Issue 2: Direct URL Access
**Symptom:** User can access restricted pages by typing URL directly
**Fix:** Decorators (@role_required) should block access at route level

### Issue 3: WAREHOUSE Can't Update Inventory
**Symptom:** WAREHOUSE role gets "Insufficient permissions" on inventory update
**Fix:** Ensure WAREHOUSE is included in @role_required decorator on /inventory/update route

### Issue 4: Error After Login
**Symptom:** "KeyError: 'role'" or similar
**Fix:** Ensure session is populated correctly in login route

## Audit Trail Verification

After testing each role:
1. Login as `admin`
2. Navigate to Users page (if audit log viewer is implemented)
3. Check that all actions are logged with:
   - User ID and Username
   - Action type (LOGIN, LOGOUT, CREATE, UPDATE, DELETE)
   - Table name
   - Record ID (if applicable)
   - Timestamp
   - IP address

## Expected Decorator Coverage

### Routes with @login_required (all authenticated users)
- / (index)
- /suppliers
- /products
- /warehouses
- /inventory
- /inventory/low-stock
- /orders
- /orders/<id>
- /analytics

### Routes with @role_required('ADMIN', 'MANAGER')
- /suppliers/add
- /suppliers/edit/<id>
- /products/add
- /warehouses/add
- /orders/create
- /orders/status/<id>

### Routes with @role_required('ADMIN', 'MANAGER', 'WAREHOUSE')
- /inventory/update/<id>

### Routes with @role_required('ADMIN')
- /suppliers/delete/<id>
- /products/delete/<id>
- /users (all user management routes)

## Success Criteria

✅ **All tests pass when:**
1. Each role can only access features specified in their permission matrix
2. Action buttons are hidden for unauthorized operations
3. Direct URL access to restricted routes returns "Insufficient permissions"
4. No server errors occur during normal operation
5. All create/update/delete operations are logged in audit_log table
6. Session management works correctly (login/logout)

## Database Verification

Run these queries as system user to verify audit logging:

```sql
-- Check recent audit logs
SELECT * FROM audit_log ORDER BY log_id DESC FETCH FIRST 20 ROWS ONLY;

-- Count actions by user
SELECT username, COUNT(*) as action_count 
FROM audit_log 
GROUP BY username 
ORDER BY action_count DESC;

-- Check specific user actions
SELECT action, table_name, TO_CHAR(action_time, 'YYYY-MM-DD HH24:MI:SS') 
FROM audit_log 
WHERE username = 'manager' 
ORDER BY action_time DESC;
```

## Troubleshooting Commands

If you encounter issues, check:

```python
# In Python shell or add to app.py temporarily
from auth import get_permissions

# Check permissions structure
print(get_permissions('ADMIN'))
print(get_permissions('MANAGER'))
print(get_permissions('WAREHOUSE'))
print(get_permissions('VIEWER'))
```

```sql
-- Check users exist
SELECT user_id, username, role, is_active FROM app_users;

-- Check password hash (should be same for all test accounts)
SELECT username, password FROM app_users WHERE username = 'admin';
-- Expected: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```
