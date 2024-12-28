CREATE DATABASE quizzdb;
CREATE USER 'dev'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `quizzdb` . * TO 'dev'@'localhost';
FLUSH PRIVILEGES;
