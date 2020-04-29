import sqlite3 as s

conn = s.connect("./MYDB")      # DB 연결
c = conn.cursor()           # 쿼리를 던지기 위해 사용

# c.execute('drop table if exists tab')
# c.execute('create table tab(menu char(20), price int)')
#
# c.execute('insert into tab values("햄버거", 5000)')
# c.execute('insert into tab values("짜장면", 6000)')
# c.execute('insert into tab values("비빔밥", 7000)')
#
# conn.commit()

c.execute('select * from tab')
k = c.fetchall()

for row in k:
    print(f'{row[0]}, {row[1]}')

c.close()
conn.close()