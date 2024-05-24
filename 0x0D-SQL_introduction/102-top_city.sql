-- This script displays the top 3 cities in July and
-- August measuring their average temperatures
-- The data was imported from a dump table called
-- temperatures.sql

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
WHERE `month`(date) IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
