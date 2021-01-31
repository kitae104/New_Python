import sqlite3

con= sqlite3.connect('test1.db')
cur = con.cursor()

search = "SELECT id, name, grade, filename FROM student"
cur.execute(search)
rows=cur.fetchall()
for row in rows :
  print(row)

sql = "SELECT img, filename FROM student WHERE id = :id"
param = {'id': 20210101}
cur.execute(sql, param)
path = cur.fetchone()
print(path[0], path[1])
fn = '/data/test.jpg'
with open(fn, 'wb') as output_file:
    output_file.write(path[0])
con.commit()
con.close()

import matplotlib.pyplot as plt
from PIL import Image
img = Image.open(fn)
print(img.size)
plt.imshow(img)
plt.show()

