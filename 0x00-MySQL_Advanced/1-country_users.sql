-- Create a table named users
-- IF table exists, should not throw error
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
       	email VARCHAR(255) UNIQUE NOT NULL,
       	name VARCHAR(255) NOT NULL,
	country ENUM("US", "CO", "TN") NOT NULL DEFAULT "US"
);  
