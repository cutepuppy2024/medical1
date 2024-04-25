student = []

# 두 명 이상의 학생의
# 이름, 국, 영, 수 점수를 입력받아
stu_name1 = input('첫번째 학생의 이름을 입력하세요 >>')
kor1 = int(input('국어성적을 입력하세요 >>'))
eng1 = int(input('영어 성적을 입력하세요 >>>'))
math1 = int(input('수학 성적을 입력하세요 >>>'))
total1= int(kor1+eng1+math1)
avg1 = float(total1) /3

stu_name2 = input('두번째 학생의 이름을 입력하세요 >>')
kor2 = int(input('국어성적을 입력하세요 >>'))
eng2 = int(input('영어 성적을 입력하세요 >>'))
math2 = int(input('수학 성적을 입력하세요 >>'))
total2 = int(kor2 + eng2 + math2)
avg2 = float(total2)/3
# 리스트를 생성 후
stu1 = [stu_name1,kor1,eng1,math1,total1,avg1]
stu2 = [stu_name2,kor2,eng2,math2,total2,avg2]
# student리스트에 넣어주세요
student.append(stu1)
student.append(stu2)
# student 리스트 전체 출력
print(student)


# 풀이
studentA =[]
stuP =[]
name = input('이름을 입력하세요 >>')
kor = int(input('국어점수를 입력하세요 >>'))
eng= int(input('영어점수를 입력하세요 >>'))
math = int(input('수학점수를 입력하세요 >>'))
# 리스트에 값 넣기
# 방법1
stuP =[name, kor,eng,math]
print(stuP)
stuP.append(kor+eng+math)  #총점
stuP.append((kor+eng+math)/3)  #평균
student.append(stu1)
print(student)

# 방법2
stuQ =[] 
stuQ.append(name)
stuQ.append(kor)
stuQ.append(eng)
stuQ.append(math)
print(stuQ)
# 방법3
stuR = ['',0,0,0] #기본값 설정 길이 설정
stuR[0] = input('이름을 입력하세요 >>')
stuR[1] = int(input('국어점수를 입력하세요 >>'))
stuR[2] = int(input('영어점수를 입력하세요 >>'))
stuR[3] = int(input('수학점수를 입력하세요 >>'))


