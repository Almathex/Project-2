CREATE TABLE IF NOT EXISTS prizedb
(
id INTEGER NOT NULL AUTO_INCREMENT,
code VARCHAR(8) NOT NULL,
reward VARCHAR(100) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 
