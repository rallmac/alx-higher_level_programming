-- This script works like the previous script
-- it imports a database from hbtn--- into my own MySQL
SELECT CONCAT(tv_shows.title, ' - ', SUM(tv_show_genres.rating))
AS show_rating FROM tv_shows JOIN tv_show_genres
ON (link unavailable) = tv_show_genres.show_id
GROUP BY tv_shows.title ORDER BY 
  SUM(tv_show_genres.rating) DESC;
