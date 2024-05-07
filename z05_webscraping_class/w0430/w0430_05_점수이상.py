import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# 점수를 입력받아 입력한 평균점수 이상의 학생을 출력하시오
# 반복해서 진행하고 -1을 입력받으면 프로그램을 종료하시오.


while True:
    sql = f'select name, avg from stu_score where avg>=(select avg(total) from stu_score) order by no'

    search = input("점수를 입력하세요 >>")
    if search == '-1':
        break
    
    print("1. 점수이상")
    print("2. 점수미만")
    num_str = input("점수이상 또는 이하를 선택하세요 >> ")
    if num_str == '1':
        sql = f'select name, avg from stu_score where avg>={search} order by no'
    else:
        sql = f'select name, avg from stu_score where avg<{search} order by no'
        
    cursor.execute(sql)
    data = cursor.fetchall()
    
    for d in data:
        print(d)
        print("-"*40)
        print("검색된 데이터 개수 :", len(data))
        print()
          
print("프로그램을 종료합니다")
conn.close()
        
        