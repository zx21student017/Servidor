CREATE USER 'logReg'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'logReg'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `logReg`;
GRANT ALL PRIVILEGES ON `logReg`.* TO 'logReg'@'localhost'; 

CREATE TABLE tabla(
    id int NOT NULL AUTO_INCREMENT,
    nombre varchar(250) NOT NULL,
    pass varchar(250) NOT NULL,
    correo varchar(500) NOT NULL UNIQUE,
    roll int NOT NULL,
    PRIMARY KEY (id)
);