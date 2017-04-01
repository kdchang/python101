import sqlite3

conn = sqlite3.connect('SimpleDB.sqlite')

cursor = conn.cursor()

#sqlstr = 'INSERT INTO user ("id", "username") VALUES ("1", "Jack")'

#cursor.execute(sqlstr)

#cursor = conn.execute('SELECT * FROM user')
#rows = cursor.fetchall()

#cursor = conn.execute('UPDATE user SET username="Jack" WHERE username="Leo"')

cursor.execute('DELETE FROM user WHERE username="Jack"')

#print(rows)



conn.commit()

conn.close()