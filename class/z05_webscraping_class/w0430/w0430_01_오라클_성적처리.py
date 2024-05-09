import oracledb

# sql
conn = oracledb.connect(user="ora_user",password='1111', dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성

# < stu_score에서 이름에 a를 포함한 사람을 순차정렬 >
# sql = "select * from stu_score where name like '_a%' order by no asc"

# board 정보에서 id, name 포함해서 데이터를 가져와 출력하시오
# board 테이블 id, member 테이블에 name
# < board 테이블 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력하시오 >
# sql = "select bno,id,name, btitle,bcontent,dbdate,bgroup,bstep,bindent,bhit,bfile from board a, member b where a.id = b.id"

# < stu_score에서 번호, 이름, 합계, 평균, grade 출력 >
# sql = """select no,name, total, avg, avg,
# case
# when avg>=90 then 'A'
# when avg>=80 then 'B'
# when avg>=70 then 'C'
# when avg>=60 then 'D'
# else 'F'
# end as grade
# from stu_score"""

# < 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오 >
# 학번, 이름, 합계, 평균, 학점
sql = "select * from stu_score"
cursor.execute(sql)       # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall()  # fetchall() : 모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴 

print("[ 모든 데이터 출력 ]")
# print(data)
for d in data[:5]:
    # print(d)
    print("평균 :",d[6])
    if d[6] >= 90 :
        print("grade :", "A")
    elif d[6] >= 80 :
        print("grade","B")
    elif d[6] >= 70 :
        print("grade","C")
    elif d[6] >=60 :
        print("grade","D")
    else :
        print("grade", "F")    
    
    print("-"*20)
print("-")
print("타입 :",type(data))

# < 월급의 평균을 출력하시오 >
# sql = "select round(avg(salary),2) as salary from employees"
# cursor.execute(sql)
# data = cursor.fetchone()
# print(data)


# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data:
#     print(d)
#     print("-"*20)
# print("-")
# print("타입 :",type(data))

