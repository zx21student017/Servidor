CREATE USER 'ventacamiones'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'ventacamiones'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `ventacamiones`;GRANT ALL PRIVILEGES ON `ventacamiones`.* TO 'ventacamiones'@'localhost'; 

CREATE TABLE camiones (
    id int NOT NULL AUTO_INCREMENT,
    marca varchar(255),
    modelo varchar(255),
    descripcion varchar(255),
    precio float(10),
    imagen varchar(255),
    fechaCreacion datetime,
    PRIMARY KEY (id)
);
 
INSERT INTO
`camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`,fechaCreacion)
VALUES ('Volvo','FH 500','seminuevo',58500,'volvo.png',now());
 
INSERT INTO
`camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`,fechaCreacion)
VALUES ('Scania','R 450 NTG','Siempre en garage',78500,'scania.png',now()-1);

INSERT INTO
`camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`,fechaCreacion)
VALUES ('Toyota','corona','nuevo',1000000,'toyota.png',now());
