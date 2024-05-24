-- This script imports a table into my database called
-- hbtn_0c_0

SELECT `city`, AVG(`temperature`) AS `avgerage_temperature`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avgerage_temperature` DESC;
