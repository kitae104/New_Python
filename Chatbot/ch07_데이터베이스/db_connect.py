# DB 호스트 연결 및 닫기
# 테이블 생성하기
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

    # 테이블 생성 sql 정의
    sql = '''
        CREATE TABLE tb_student (
            id int primary key auto_increment not null,
            name varchar(32),
            age int,
            address varchar(32)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('DB 닫기 성공')
