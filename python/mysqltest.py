import mysql.connector
# .py name should not be mysql.py

# do not push password to github
# get a connection from localhost
conn = mysql.connector.connect(user="root",password="********",database="test")

# get cursor
cursor = conn.cursor()
# execute command with tran
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.close()
# execute once

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
print(cursor.fetchall())
cursor.close()
conn.close()
