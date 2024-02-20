# from model.connection import Conn
# email = "dinesh07@gmail.com"
# query = "SELECT PASS,USERNAME FROM USER WHERE EMAILID = ? OR USERNAME = ?"
# connection = Conn.get_connection().connection
# cursor = connection.cursor()
# cursor.execute(query,email,email)
# rows = cursor.fetchall()
# print(rows[0][0])
#
# import
#
# p = getpass.getpass("Enter pass: ")
# print(p)

import os
a = os.environ.get('password')
print(a)