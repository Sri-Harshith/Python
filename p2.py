import sqlite3
from sqlite3 import*
con=connect('db_file')
con.execute("CREATE TABLE CLASS_10(ID INT PRIMARY KEY NOT NULL,FIRST NAME TEXT NOT NULL,LAST NAME TEXT NOT NULL,ADDRESS TEXT NOT NULL, EMAIL ID CHAR(30));")
con.close()