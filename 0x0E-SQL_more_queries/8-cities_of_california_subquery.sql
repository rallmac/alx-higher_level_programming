-- This script lists cities in California database hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM state
	WHERE name = "California")
ORDER BY id;
