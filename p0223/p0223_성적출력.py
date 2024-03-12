# 출력

#리스트를 사용해서 출력
stu_no1 = 1
stu_name1 = '홍길동'
kor1 = 100
eng1= 100
math1 = 100
total1 = kor1+eng1+math1
avg1 = total1/3
rank1 = 0


stu1 = [1,'홍길동',100,100,100,300,100.0,1]
stu2 = [2,'유관순',90,90,90,270,90.0,2]
stu3 = [3,'이순신',80,90,70,240,80.0,3]



print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu_no1,stu_name1,kor1,eng1,math1,total1,avg1,rank1
))

# stu_no = input("학생번호를 입력하세요>>")

print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))


print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('0. 프로그램 종료')
print('-'*35)

choice = int(input('원하는 번호를 입력하세요 >>'))
# 1번을 입력하면 [학생성적입력을 선택하셨습니다] 출력
# 4번을 입력하면 학생성적전체출력

if choice == 1:
    print('학생성적입력을 선택하셨습니다')
    stu_name = input("이름을 입력하세요 >>")
    kor = int(input('국어성적을 입력하세요 >>'))
    eng = int(input('영어성적을 입력하세요 >>'))
    math = int(input('수학성적을 입력하세요 >>'))
    stu3 =[3,stu_name,kor,eng,math,kor+eng+math,(kor+eng+math)/3,3]
    print(stu3)
elif choice == 4 :
    print('학생성적전체출력')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        stu3[0],stu3[1],stu3[2],stu3[3],stu3[4],stu3[5],stu3[6],stu3[7]))
elif choice == 0 :
    print('프로그램을 종료합니다')
else :
    print('잘못 누르셨습니다')
    