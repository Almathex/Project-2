CREATE TABLE IF NOT EXISTS Prize
(
id INTEGER NOT NULL AUTO_INCREMENT,
random_string VARCHAR(8) NOT NULL,
prize VARCHAR(100) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 
