-- Create a table named users
-- IF table exists, should not throw error
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       	email VARCHAR(255) NOT NULL UNIQUE,
       	name VARCHAR(255) NOT NULL,
);  
