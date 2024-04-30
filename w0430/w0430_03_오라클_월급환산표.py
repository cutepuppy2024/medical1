import oracledb
 
# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor()

# sql 실행구문
# sql = ""
# cursor.execute(sql)
# data = cursor.fetchall()

# <  employees 테이블에서 사번, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급*1410 원화로 환산해서 천단위표시해서 출력  >
sql = "select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_sal, to_char(salary*1410,'999,999,999') kor_salary from employees"
cursor.execute(sql)
data = cursor.fetchall()

print("[ 데이터 출력 ]")
print("-"*40)
print("사원번호\t사원명\t월급\t실제월급\t원화환산")
print("-"*40)
for d in data:
    # print(d)
    print(d[0],end="\t")
    print(d[1],end="\t")
    print(d[2],end="\t")
    print(d[3],end="\t")
    print("￦",d[4].strip())
    
    
# 부서별 평균월급, 최대월급, 최소월급을 출력하시오
# sql = """select department_id,count(department_id), round(avg(salary),2), max(salary), min(salary) from employees
#         where department_id is not null
#         group by department_id
#         order by department_id"""
# cursor.execute(sql)
# data = cursor.fetchall()  
# print("[ 데이터 출력 ]")
# print("부서명\t부서사원수\t평균월급\t최대월급\t최소월급")
# print("-"*40)
# print("-"*40)
# for d in data:
#     print(d[0],end="\t")
#     print(d[1],end="\t")
#     print(d[2],end="\t")
#     print(d[3],end="\t")
#     print()


