CREATE TABLE IF NOT EXISTS prizedb
(
id INTEGER NOT NULL AUTO_INCREMENT,
random_string VARCHAR(8) NOT NULL,
winnings VARCHAR(100) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 
