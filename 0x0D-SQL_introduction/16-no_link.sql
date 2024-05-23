-- This script list all the records in the table second_table
-- of the database hbtn_0c_0
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
