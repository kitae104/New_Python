import sqlite3

con = sqlite3.connect("test1.db")
print(sqlite3.version)
cur = con.cursor()
q="DROP TABLE IF EXISTS student"
cur = con.cursor()
q="CREATE TABLE student(id INTEGER NOT NULL PRIMARY KEY,name  TEXT NOT NULL,grade  INTEGER, path TEXT)"
cur.execute(q)
data = (20210101,'kim', 1, '/data/b1.jpg')
sql = "INSERT INTO student VALUES (?,?,?,?)"
cur.execute(sql, data)
data = (20210102,'Lee', 2, '/data/b2.jpg')
sql2 = "INSERT INTO student VALUES (?,?,?,?)"
cur.execute(sql2, data)
search = "SELECT id, name, grade FROM student"
cur.execute(search)
rows=cur.fetchall()
for row in rows :
  print(row)

sql = "SELECT path FROM student WHERE id = :id"
param = {'id': 20210101}
cur.execute(sql, param)
path = cur.fetchone()
print(path[0])



con.commit()
con.close()