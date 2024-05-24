-- This script displays the maximum temperture of each state
-- ordered by the state name, of an imported dump table
-- called temperatures.sql

mysql -u -p hbtn_0c_0 < temperatures.sql

SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
