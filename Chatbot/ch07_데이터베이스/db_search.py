# 데이터 조회
import pymysql
import pandas as pd

db = None

try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='kitae',
        passwd='1111',
        db='jpa',
        charset='utf8'
    )
    print('DB연결 성공')

    # 데이터 정의
    students = [
        {'name': 'Kitae', 'age': 30, 'address' : 'PUSAN'},
        {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
        {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
        {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
        {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    ]

    # 데이터 db에 추가
    for s in students:
        with db.cursor() as cursor:
            sql = '''
                insert tb_student(name, age, address) values ("%s", %d, "%s")
            ''' % (s['name'], s['age'], s['address'])
  #          cursor.execute(sql)

  #  db.commit()

    # 30대 학생만 조회
    cond_age = 30

    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from tb_student where age >= %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()     # 전체 불러오기
    print(results)

    # 이름 검색
    cond_name = 'Grace'

    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
            select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()      # 하나만 불러오기

    print(result['name'], result['age'])

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
