import oracledb

conn = oracledb.connect(user="ora_user",password='1111', dsn="localhost:1521/xe")
cursor = conn.cursor()


# 찾고자 하는 이름 또는 단어
while True:
    search = input("찾고자 하는 이름을 입력하세요 >> (-1: 종료)")
    if search == '-1': 

        break

    sql = f"""select * from stu_score
            where name like '%{search}%'
            order by no"""
    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        print(d)
        
    print("검색된 데이터 개수 :", len(data))
    print()
        
print("프로그램을 종료합니다")      
conn.close()