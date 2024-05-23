-- This script inserts four records into a table called
-- second_table in a database called hbtn_0c_0
-- the records are key, name and score
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256),score INT);

-- This script creates a maximum of 4 records
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
