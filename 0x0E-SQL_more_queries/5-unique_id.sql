-- This script creates a tabe 'unique_id on the server'
CREATE TABLE IF NOT EXISTS unique_id
	(id INT DEFAULT 1,
	UNIQUE (ID),
	name VARCHAR(256));
