import sqlite3

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

con= sqlite3.connect('test1.db')
cur = con.cursor()
q="DROP TABLE IF EXISTS student"
cur = con.cursor()
cur.execute(q)
q="CREATE TABLE student(id INTEGER NOT NULL PRIMARY KEY,name  TEXT NOT NULL,grade  INTEGER, filename TEXT, img BLOB)"
cur.execute(q)
img_pic = convertToBinaryData("/data/b1.jpg")
data = (20210101,'kim', 1, "/data/b1.jpg", img_pic)
sql = "INSERT INTO student VALUES (?,?,?,?,?)"
cur.execute(sql, data)
img_pic = convertToBinaryData("/data/b2.jpg")
data = (20210102,'Lee', 2, "/data/b2.jpg",img_pic)
sql2 = "INSERT INTO student VALUES (?,?,?,?,?)"
cur.execute(sql2, data)
search = "SELECT id, name, grade, filename FROM student"
cur.execute(search)
rows=cur.fetchall()
for row in rows :
  print(row)

sql = "SELECT filename, img FROM student WHERE id = :id"
param = {'id': 20210101}
cur.execute(sql, param)
path = cur.fetchone()
print(path[0])

con.commit()
con.close()