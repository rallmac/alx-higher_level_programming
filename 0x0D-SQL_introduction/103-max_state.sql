-- This script displays the maximum temperture of each state
-- ordered by the state name, of an imported dump table
-- called temperatures.sql

SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
