student = []

#for 를 사용해서 5번 반복
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
        stu1 = [name,kor,eng,math]
        student.append(stu1)
        print(stu1)
        print(student)

    elif ch == '4' :
        print('학생성적전체출력')
        print('이름\t국어\t영어\t수학')
        # 출력       
        for i in range(len(student)):
            print('{}\t{}\t{}\t{}'.format(name,kor,eng,math))
            print(student[0][0], student[0][1], student[0][2], student[0][3])
        
    elif ch == '0' :
        print('프로그램 종료')
    else:
        print('잘못 누르셨습니다')
    print('-'*35)
    print('-'*35)
