-- This script works like the previous script
-- it imports a database from hbtn_0d_tvhsows
-- into my own MySQL
SELECT CONCAT(tv_genres.name, ' - ', SUM(tv_show_genres.rating)) 
AS genre_rating FROM tv_genres JOIN tv_show_genres ON
(link unavailable) = tv_show_genres.genre_id GROUP BY
tv_genres.name ORDER BY SUM(tv_show_genres.rating) DESC;
