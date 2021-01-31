import sqlite3

con= sqlite3.connect('test1.db')
cur = con.cursor()

sql = "SELECT img, filename FROM student WHERE id = :id"
param = {'id': 20210102}
cur.execute(sql, param)
path = cur.fetchone()
print(path[1])
fn = str(path[1])
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