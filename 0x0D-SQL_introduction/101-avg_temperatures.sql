-- This script imports a table into my database called
-- hbtn_0c_0
mysql -u -p hbtn_0c_0 < temperatures.sql

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
