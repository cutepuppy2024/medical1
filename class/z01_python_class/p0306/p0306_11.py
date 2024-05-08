# students = [
#     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
#     {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
#     {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
#     {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
#     {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

#학생성적 입력부분 구현하시오.

students =[]
cnt = 0
while True:
    ch = input('원하는 작업을 입력하세요>> (1.학생성적입력  2.학생성적전체출력  0.프로그램종료)')
    ch = int(ch)
    if ch == 1 :
        print('학생성적 입력을 선택하셨습니다.')
        while True:
            name = input("이름을 입력하세요 (0.취소)>>")
            if name == '0':
                break
            student = {}
            cnt =+ 1
            student['stuNo'] = 'S'+'{:03d}'.format(cnt)
            student['name'] = name
            kor = int(input('국어성적을 입력하세요 >>'))
            student['kor'] = kor
            eng = int(input('영어성적을 입력하세요 >>'))
            student['eng'] = eng
            math = int(input('수학성적을 입력하세요 >>'))
            student['math'] = math
            total = kor + eng + math
            student['total'] = total
            avg = "{:.2f}".format(total/3)
            student['avg'] = avg
            print(student)
            students.append(student)
            print(students)
        
    elif ch == 2 :
        print('학생성적전체출력을 선택하셨습니다')
        print('-'*65)
        print('\t[ 학생성적전체출력 ]')
        print('-'*65)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*65)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
                
    elif ch == 0 :
        print('프로그램을 종료합니다')
        break
                
    

    
    