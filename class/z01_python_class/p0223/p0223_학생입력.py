# 학생성적 입력

# 변수를 사용 합니다

stu_name = '홍길동' 
kor = 100
eng = 100
math = 100


# 입력을 받아서 총점과 평균을 계산하고

stu_name = input('이름을 입력하세요 >> ')
kor = int(input("국어 성적을 입력하세요 >>"))
eng = int(input("영어 성적을 입력하세요 >>>"))
math = int(input("수학 성적을 입력하세요 >"))
total = kor+eng+math
avg = (kor+eng+math)/3

print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{} \t {} \t {} \t {} \t {} \t {} \t{} \t{}'.format(
    1,stu_name,kor,eng,math,total,avg, 1))
# 출력해 보세요
# 홍길동 100 100 100 300 100.0

stu= [1 , '홍길동', 100, 100, 100, 300, 100.0 , 1]
stu1= [1,stu_name,kor,eng,math,total,avg, 1]

print(stu)
print(stu1)