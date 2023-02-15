CREATE USER 'museo'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'museo'@'localhost' 
REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `museo`;GRANT ALL PRIVILEGES ON `museo`.* TO 'museo'@'localhost'; 

CREATE TABLE comprador(
	id INT(6) AUTO_INCREMENT NOT NULL,
	dni VARCHAR(20) NOT NULL UNIQUE,
	CONSTRAINT pk_comprador PRIMARY KEY(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

CREATE TABLE entradas(
	id INT(6) AUTO_INCREMENT NOT NULL,
	numAdultos INT(3) NOT NULL,
numMenores INT(3) NOT NULL,
	total  FLOAT(2) NOT NULL,
	id_comprador INT(6) NOT NULL,
	CONSTRAINT pk_entradas PRIMARY KEY(id),
	CONSTRAINT fk_entradas_comprador FOREIGN KEY(id_comprador) REFERENCES comprador(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

INSERT INTO comprador(dni) VALUES ("12345678D");
INSERT INTO comprador(dni) VALUES ("87654321F");