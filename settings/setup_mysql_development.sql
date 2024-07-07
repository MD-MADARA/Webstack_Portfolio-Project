-- creates the database Estore_db and the user dev-user if not exists
-- give all privileges on the database Estore_db to dev-user
-- give SELECT privilege on the database performance_schema to dev-user
DROP DATABASE IF EXISTS Estore_db;
CREATE DATABASE IF NOT EXISTS Estore_db;
CREATE USER IF NOT EXISTS 'dev-user'@'localhost' IDENTIFIED BY 'Hesoyam25$';
GRANT ALL PRIVILEGES ON Estore_db.* TO 'dev-user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'dev-user'@'localhost';
