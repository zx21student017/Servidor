CREATE USER 'biblioteca'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'biblioteca'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `biblioteca`;
GRANT ALL PRIVILEGES ON `biblioteca`.* TO 'biblioteca'@'localhost';

CREATE TABLE socios (
	id INT(6) AUTO_INCREMENT NOT NULL,
	nombre VARCHAR(20) NOT NULL UNIQUE,
	CONSTRAINT pk_socio PRIMARY KEY(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

CREATE TABLE libros(
	id INT(6) AUTO_INCREMENT NOT NULL,
	titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(50) NOT NULL,
	id_socio  INT(6) NOT NULL,
	CONSTRAINT pk_libros PRIMARY KEY(id),
	CONSTRAINT fk_libro_socio FOREIGN KEY(id_socio) REFERENCES socios(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

INSERT INTO socios(nombre) VALUES ("Pedro");
INSERT INTO socios(nombre) VALUES ("Isabel");