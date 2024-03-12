# 이름, 국어, 영어, 수학을 입력받아
# 합계를 출력하시오

# name = input('이름을 입력하세요 >>')
# kor = int(input('국어성적을 입력하세요 >>'))
# eng = int(input('영어성적을 입력하세요 >>'))
# math = int(input('수학성적을 입력하세요 >>'))
# total = kor + eng + math
# # print('합계 :',total) 
# print('합계 :', (kor + eng + math))    #github 관리 중요!! 

# java나 다른 언어는 grouping이 힘들다, 넘어가면 type을 다 나누어 주고,따로 저장해야 한다  파이썬은 grouping이 용이 즉, 다른 type을 한번에 사용가능
# 알고리즘  #기존의 입력된 정보가 한꺼번에 나오도록 파이썬이 개발중   
# 콘솔창/브라우저창  융합적으로 알아야 한다 !!

# 2명의 학생의 이름, 국어, 영어, 수학을 입력받아 
'''
kor = []  # java는 이렇게 묶는다
eng = []
math = []
total = []
'''
students = []  # 파이썬의 유리한 점  =>그러나 각 항목의 type이 어떤 형태인지 정확이 알고 있어야 한다!! #차원이 늘어날 수록 grouping이 늘어나겠지만, 2차원 이상은 복잡해져서 잘 사용하지 않는다=>class사용

for i in range(0,2) :
    student = [] # 초기화
    student.append(input('이름을 입력하세요 >>'))
    student.append(int(input('국어성적을 입력하세요 >>')))  #kor = int(input('국어성적을 입력하세요 >>'))
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
#2차원 리스트는 for문을 2번 사용함    
for stu in students:                                       # 공공데이터 # JSON파서  //  # [] 리스트 : 데이터 값만 {} 딕셔너리 : 키 값 => 가장 큰 차이점
    for s in stu:
        print(s, end='\t')                                 # 배워야 하는 것은 처리해야 하는 형태!!!  =>정보를 선별하여 가지고 오는 기술, 가지고 오는 위치 선택을 잘 해야 한다!!
    print()
print()
print('-'*30)

#총 학생의 총국어점수, 총영어점수, 총수학점수, 총합계, 총평균
kors = 0 
engs = 0
maths = 0
totals = 0
avgs = 0
for i, stu in enumerate(students):  # 번호  # 2차원 리스트에서는 enumerate 사용이 간편하고 알아보기 쉬운듯
    kors = kors + stu[1]
    engs = engs + stu[2]
    maths += stu[3]
    totals += stu[4]
avgs = totals/len(students)
print('\t')
print(kors, engs, maths, totals, avgs,sep='\t')




# 3명의 국어점수 합계, 평균을 출력하시오.

kor_sum = 0                          # enumerate 사용하지 않고 고민한 이유: for를 중첩사용해야 될거라고 생각함 -> 반복개념에 대해 명확하게!!
for i in students:
    kor_sum += i[1]
print(kor_sum)
print(kor_sum/len(students))




