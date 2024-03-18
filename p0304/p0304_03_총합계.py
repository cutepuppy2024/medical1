# 이름, 국어, 영어, 수학을 입력받아
# 합계를 출력하시오

name = input('이름을 입력하세요 >>')
kor = int(input('국어성적을 입력하세요 >>'))
eng = int(input('영어성적을 입력하세요 >>'))
math = int(input('수학성적을 입력하세요 >>'))
total = kor + eng + math
print('합계 :',total) 
print('합계 :',(kor + eng + math))    


# 2명의 학생의 이름, 국어, 영어, 수학을 입력받아 
# 합계, 평균을 추가한
# 리스트를 출력하시오
students = []  

for i in range(0,2) :
    student = [] # 초기화
    student.append(input('이름을 입력하세요 >>'))
    student.append(int(input('국어성적을 입력하세요 >>')))  
    student.append(int(input('영어성적을 입력하세요 >>')))
    student.append(int(input('수학성적을 입력하세요 >>')))
    sum = student[1] +student[2] + student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)
# 합계
print(students)


# 전체학생출력
print('[학생성적 출력]')
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
# 2차원 리스트는 for문을 2번 사용함    
for stu in students:                                       
    for s in stu:
        print(s, end='\t')                                 
    print()
print()
print('-'*30)

# 총 학생의 총국어점수, 총영어점수, 총수학점수, 총합계, 총평균
kors = 0 
engs = 0
maths = 0
totals = 0
avgs = 0
for i, stu in enumerate(students): 
    kors = kors + stu[1]
    engs = engs + stu[2]
    maths += stu[3]
    totals += stu[4]
    avgs = totals/3/len(students)
print()
print(kors, engs, maths, totals, avgs,sep='\t')


# 3명의 국어점수 합계, 평균을 출력하시오.

kor_sum = 0                          
for i in students:
    kor_sum += i[1]
print(kor_sum)
print(kor_sum/len(students))




