import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

sql = f"""create table mem (
id varchar2(30),
pw varchar2(30),
name varchar2(30),
mdate date
)"""
cursor.execute(sql)


# DDL 명령어는 commit이 없음
# DML 명령어 : insert, update, delete

print("테이블 생성완료")

cursor.close()
conn.close()