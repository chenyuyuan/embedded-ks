#!/bin/sh
DBNAME='dev.db'
rm -f $DBNAME
echo start insert data
sqlite3 $DBNAME < create_table.sql
echo insert finish
