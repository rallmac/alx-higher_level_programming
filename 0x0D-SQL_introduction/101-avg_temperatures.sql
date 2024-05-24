-- This script imports a table into my database called
-- hbtn_0c_0
mysql -u -p hbtn_0c_0 < temperatures.sql

SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
