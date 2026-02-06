from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='rootpwd',
                              host='173.194.87.90', database='employees')
cur = conn.cursor()

try:
	cur.execute("DELETE FROM employees")


	conn.commit()
except mysql.connector.Error as err:
	print(err.msg)
	exit(1)


conn.close()