import sqlite3

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

con= sqlite3.connect(':memory:')
cur = con.cursor()
q="DROP TABLE IF EXISTS student"
cur = con.cursor()
q="CREATE TABLE student(id INTEGER NOT NULL PRIMARY KEY,name  TEXT NOT NULL,grade  INTEGER, img BLOB)"
cur.execute(q)
img_pic = convertToBinaryData("b1.jpg")
data = (20210101,'kim', 1, img_pic)
sql = "INSERT INTO student VALUES (?,?,?,?)"
cur.execute(sql, data)
img_pic = convertToBinaryData("b2.jpg")
data = (20210102,'Lee', 2, img_pic)
sql2 = "INSERT INTO student VALUES (?,?,?,?)"
cur.execute(sql2, data)
search = "SELECT id, name, grade FROM student"
cur.execute(search)
rows=cur.fetchall()
for row in rows :
  print(row)

sql = "SELECT img FROM student WHERE id = :id"
param = {'id': 20210101}
cur.execute(sql, param)
img = cur.fetchone()
print(img)

con.commit()
con.close()