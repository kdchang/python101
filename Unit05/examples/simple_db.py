'''
建立連線：connect
建立 cursor 物件：cursor
執行 sql：execute
執行資料庫更新：commit
關閉資料庫連線：close

CRUD
1. Create
INSERT INTO user ("id", "username") VALUES (1, "Leo")
2. Read
SELECT * FROM user
3. Update
UPDATE user SET username="Jack" WHERE username="Leo 
4. Delete 
DELETE FROM user WHERE username="Jack"
'''

import sqlite3

conn = sqlite3.connect('SimpleDB.sqlite')

cursor = conn.cursor()

sqlstr = 'INSERT INTO user ("id", "username") VALUES (1, "Leo")'
cursor.execute(sqlstr)

# cursor = conn.execute('UPDATE user SET username="Jack" WHERE username="Leo"')
# cursor = conn.execute('DELETE FROM user WHERE username="Jack"')
# cursor = conn.execute('SELECT * FROM user')
# rows = cursor.fetchall()

conn.commit()
# print(rows)
conn.close()