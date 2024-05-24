-- This script converts the database hbtn_0c_0 to UTF8
-- it also converts the table first_table to UTF8
-- and also converts the name field 'name' to UTF8

USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
