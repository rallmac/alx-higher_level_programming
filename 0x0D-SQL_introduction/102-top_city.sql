-- This script displays the top 3 cities in July and
-- August measuring their average temperatures
-- The data was imported from a dump table called
-- temperatures.sql

mysql -u -p hbtn_0c_0 < temperatures.sql

SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
WHERE month(date) IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
