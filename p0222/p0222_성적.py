# 학생 이름, 국어, 영어, 수학 점수를 입력받아서
# 아래와 같이 출력을 하고

# 만약에 평균이 80점 이상이면 합격입니다를 출력하세요

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}  \t{}   \t{}  \t{}  \t{} \t{}  \t{}  \t{}'.format(
       1, '홍길동',100,  100,  100, 300, 100.0   ,1))
print('홍길동님 합격입니다')


num = 1
stu_name = input("학생 이름을 입력하세요 >>")
kor = input("국어 성적을 입력하세요 >>")
kor = int(kor)
eng = input("영어 성적을 입력하세요 >>")
eng = int(eng)
math = input("수학 성적을 입력하세요 >>")
math = int(math)
total = kor+eng+math
avg = (kor+eng+math)/5
print('번호\t학생이름\t국어\t영어\t수학\t합계\t평균')
print('{} \t   {}   \t {} \t{} \t{}  \t{} \t{:.2f}'.format(
       num,stu_name,kor,  eng, math, total,avg))

if avg >= 60 :                        #if문은 들여쓰기가 중요하다!!! 활용하여 login/password까지 가능
    print(stu_name+"님 합격입니다")    #('{}님 합격입니다'.format(stu_name))
else:
    print(stu_name+"님 불합격입니다")



#-------------------------------------------------------
# 문제 만들어보기
    
num = input("학생 번호를 입력하세요")
stu_name = input("학생 이름을 입력하세요 >>")
kor = input("국어 성적을 입력하세요 >>")
kor = int(kor)
eng = input("영어 성적을 입력하세요 >>")
eng = int(eng)
math = input("수학 성적을 입력하세요 >>")
math = int(math)
soc = input("사탐성적을 입력하세요 >>")
soc = int(soc)
sci = input("과탐성적을 입력하세요 >>")
sci = int(sci)
total = kor+eng+math+soc+sci
avg = (kor+eng+math+soc+sci)/5
print('번호\t학생이름\t국어\t영어\t수학\t사탐\t과탐\t총점\t평균')
print('{} \t{}      \t{} \t{}  \t{} \t {} \t{} \t{}   \t{}'.format(
    num,stu_name,kor,eng,math,soc,sci,total,avg
))

if avg >= 60 :                        #if문은 들여쓰기가 중요하다!!! 활용하여 login/password까지 가능
    print(stu_name+"님 합격입니다")    #('{}님 합격입니다'.format(stu_name))
else:
    print(stu_name+"님 불합격입니다")

if kor <= 40 or eng <= 40 or math <= 40 :
    print(stu_name+"님 과락입니다") 
else :
    print(stu_name+"님 과락은 아닙니다")
    
if kor >=99.5 and eng >=99.9 and math >=98 :
    print(stu_name+"님 의대 지원 가능합니다")
else:
    print(stu_name+"님 의대는 어렵습니다")