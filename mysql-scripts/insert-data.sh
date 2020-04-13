#!/bin/bash
MYSQL_PASSWORD=$(grep MYSQL_PASSWORD ../.env | cut -d '=' -f2)
docker exec mysql /bin/sh -c 'mysql -u user -p$MYSQL_PASSWORD db < /mysql-scripts/insert-data.sql'
