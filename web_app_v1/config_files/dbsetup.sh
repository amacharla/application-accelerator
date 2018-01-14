#!/usr/bin/env bash
  
EXPECTED_ARGS=1
E_BADARGS=65
MYSQL=$(which mysql)
  
Q1="CREATE DATABASE IF NOT EXISTS $1;"
Q2="GRANT USAGE ON *.* TO 'flask'@'%' IDENTIFIED BY 'f1ask';"
Q3="GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON $1.* TO 'flask'@'%';"
Q4="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}${Q3}${Q4}"
  
if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: dbname"
  exit $E_BADARGS
fi
  
$MYSQL -uroot -pr00t -e "$SQL"
