-- This script converts the database hbtn_0c_0 to UTF8
-- it also converts the table first_table to UTF8
-- and also converts the name field 'name' to UTF8
# Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

# Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Convert the name field to UTF8
ALTER TABLE first_table CHANGE name name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
