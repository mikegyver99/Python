from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='rootpwd',
                              host='173.194.87.90')
cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE employees DEFAULT CHARACTER SET 'utf8'")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database already exists, continuing...")
    else:
        print("Failed creating database: {}".format(err))
        exit(1)

conn.database = "employees"
try:
    cur.execute(
        "CREATE TABLE `employees` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ") ENGINE=InnoDB")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("employees table already exists.")
    else:
        print(err.msg)

conn.close()