import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# 저장하기
sql = "insert into member values (member_seq.nextval, 'ggg',1111,'홍길순','여자',sysdate)"
cursor.execute(sql)
cursor.execute("commit")

# 저장, 변경, 삭제 (insert, update, delete) 모두 같음
# sql = "update member set name='홍길동' where id='aaa"
# cursor.execute(sql)
# cursor.execute("commit")

# sql 읽어오기
# fetchone(), fetchall()
sql = 'select * from member'
cursor.execute(sql)
data = cursor.fetchall()

for d in data :
    print(d)

cursor.close()
