-- creates the database hbnb_dev_db and the user hbnb_dev if not exists
-- give all privileges on the database hbnb_dev_db to hbnb_dev
-- give SELECT privilege on the database performance_schema to hbnb_dev
DROP DATABASE IF EXISTS ecom_db;
CREATE DATABASE IF NOT EXISTS ecom_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON ecom_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
