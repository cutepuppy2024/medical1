# student = [[1, '홍길동',100,100,100,300,100.0,1],
#            [2, '유관순',90,90,90,270,90.0,1]]

# stu1 = student[0]
# stu2 = student[1]

# print('-'*35)
# print('\t[학생성적프로그램]')
# print('1.학생성적입력') # 1명만 입력 print(student)
# print('4.학생성적전체출력') # 2명이 출력
# print('-'*35)

# ch = input('원하는 번호를 입력하세요 >>')
# if ch == '1' :
#     print('학생 성적을 입력을 선택하셨습니다')
#     # student.append([3, '이순신', 90,85,95,270,90.0,1])
#     # print(student)
#     stu3 = ['',0,0,0]
#     stu3.append[''] = input('이름을 입력하세요 >>')
#     stu3.append[1] = int(input('국어성적 >>'))
#     stu3.append[2] = int(input('영어성적 >>'))
#     stu3.append[3] = int(input('수학성적 >>'))
#     print(stu3)

#     print(stu3)
# if ch == '4' :
#     print('학생성적출력')
#     print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
#     print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
#       stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7] # 줄바꾸기 -
#       stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]
    # ))
    # print(student)  

student = [[1, '홍길동',100,100,100,300,100.0,1],
           [2, '유관순',90,90,90,270,90.0,1]]

# 풀이
print('-'*35)
print('\t[학생성적프로그램]')
print('1.학생성적입력') # 1명만 입력 print(student)
print('4.학생성적전체출력') # 2명이 출력
print('-'*35)

ch = input('원하는 번호를 입력하세요 >>')        #간단하게, 주어진 정보를 활용해서 
if ch == '1':
    print('학생성적입력')
    name = input('이름을 입력하세요 >>')
    kor = int(input('국어점수를 입력하세요 >>'))
    eng = int(input('영어점수를 입력하세요 >>'))
    math = int(input('수학점수를 입력하세요>>'))
    total = kor+eng+math
    avg = total/3
    # stu1 = [3,name,kor,eng,math,total,avg,1]
    stu1 = [3,name,kor,eng,math]
    stu1.append(total)
    stu1.append(avg)
    stu1.append(3)
    
    student.append(stu1)
    print(stu1)
    print(student)

elif ch == '4': # 학생성적 전체출력
    print('학생성적출력')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],student[0][6],student[0][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],student[1][5],student[1][6],student[1][7]))