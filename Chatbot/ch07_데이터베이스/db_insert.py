# DB에 데이터 입력하기
import pymysql
import cryptography

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

    # 데이터 삽입 sql 정의
    sql = '''
        INSERT tb_student(name, age, address) values('kitae', 20, 'Korea')
        '''
    
    # 데이터 삽입
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('DB 닫기 성공')
