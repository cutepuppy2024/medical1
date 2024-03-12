student = []
for i in range(10):
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch= input('원하는 번호를 입력하세요 >>')
    print(ch)
    # if 문을 사용해서 1 누르면 [학생성적입력]
    if ch == '1':                           #들여쓰는 것 연습하는 중
        print('학생성적입력')
        name = input('학생 이름을 입력하세요 >>')
        kor = int(input('국어 성적을 입력하세요 >>'))
        eng = int(input('영어 성적을 입력하세요 >>'))
        math = int(input('수학 성적을 입력하세요 >>'))
        stu1 = [1,name,kor,eng,math,(kor+eng+math),(kor+eng+math)/3] #한명의 학생의 정보를 담은 리스트
        student.append(stu1)
        print(stu1)
        print(student)
    elif ch == '4' :
        print('학생성적전체출력')
        print('이름\t국어\t영어\t수학\t총점\t평균')
        for i in range(len(student)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            student[i][0], student[i][1], student[i][2], student[i][3],student[i][4],student[i][5],student[i][6]))
    elif ch == '0' :
        print('프로그램 종료')
    else:
        print('잘못 누르셨습니다')
print('-'*35)
print('-'*35)
              
    # # 4 누르면 [학생성적전체출력]
    # # 0 누르면 [프로그램 종료]