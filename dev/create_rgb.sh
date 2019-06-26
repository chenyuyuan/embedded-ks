#!/bin/sh
DBNAME='rgb.db'
rm -f $DBNAME
echo start insert data
sqlite3 $DBNAME < create_rgb.sql
echo insert finish
