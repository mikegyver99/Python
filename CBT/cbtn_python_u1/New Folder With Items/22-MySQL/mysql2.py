from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='rootpwd',
                              host='173.194.87.90', database='employees')
cur = conn.cursor()

try:
	cur.execute("INSERT INTO employees "
			"(first_name, last_name, hire_date) "
			"VALUES( 'Ben', 'Finkel', '2008-01-01' )")
	cur.execute("INSERT INTO employees "
			"(first_name, last_name, hire_date) "
			"VALUES( 'Alice', 'Smith', '2010-07-15' )")
	cur.execute("INSERT INTO employees "
			"(first_name, last_name, hire_date) "
			"VALUES( 'Bob', 'Jones', '1997-10-10' )")

	conn.commit()
except mysql.connector.Error as err:
	print(err.msg)
	exit(1)

try:
	cur.execute("SELECT first_name, last_name, hire_date "
			"FROM employees WHERE hire_date > '2000-01-01' ")
except mysql.connector.Error as err:
	print(err.msg)
	exit(1)

for (first_name, last_name, hire_date) in cur:
	print(first_name,last_name,hire_date)	

conn.close()