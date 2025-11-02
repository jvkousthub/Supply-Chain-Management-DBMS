-- Migration: Update VIEWER role to CUSTOMER role
-- Run this script to rename VIEWER to CUSTOMER throughout the database

-- Step 1: Update existing VIEWER users to CUSTOMER
UPDATE app_users 
SET role = 'CUSTOMER' 
WHERE role = 'VIEWER';

-- Step 2: Drop existing constraint
ALTER TABLE app_users DROP CONSTRAINT SYS_C008405;

-- Step 3: Add new constraint with CUSTOMER instead of VIEWER
ALTER TABLE app_users 
ADD CONSTRAINT chk_role 
CHECK (role IN ('ADMIN', 'MANAGER', 'WAREHOUSE', 'CUSTOMER'));

COMMIT;

-- Verify the changes
SELECT username, role, full_name FROM app_users ORDER BY role;

SELECT 'Migration completed! VIEWER role changed to CUSTOMER' AS status FROM DUAL;
