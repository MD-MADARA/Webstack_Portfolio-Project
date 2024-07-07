#!/bin/bash
echo "clean database and setup new one, root password is needed ..."
sleep 1
settings/clean_db

sleep 1
echo "adding  product objects ..."
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=ecom_db python3   -m settings.add_products
sleep 1
echo "done!"
