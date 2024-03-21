students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
             {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
             {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
             {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
             {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
            ]

cnt = len(students)

while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생성적수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자를 입력하세요')
        continue  # => 반복문이 계속 되어야 한다
    choice = int(choice)
    if choice == 1:
        print('학생성적입력을 선택하셨습니다.')
        student = {}
        for i in range(5):
            student['rank'] = 1
        name = input('학생 이름을 입력하세요 (0. 취소)>')
        if name == '0':
            break
        
        cnt += 1
        stuNo = 'S' + '{:03d}'.format(cnt)
        student['stuNo'] = stuNo
        student['name'] = name
        kor = int(input('국어성적을 입력하세요 >'))
        student['kor'] = kor
        eng = int(input('영어성적을 입력하세요 >'))
        student['eng'] = eng
        math= int(input('수학성적을 입력하세요 >'))
        student['math'] = math
        total = kor + eng + math
        student['total'] = total
        avg = total/3
        student['avg'] = float('{:.2f}'.format(avg))
        student['rank'] = 1
        students.append(student)
        print(students)
        
    elif choice == 2:
        print('학생성적전체출력을 선택하셨습니다.')
        p_select = int(input('출력하시겠습니까? (1.출력 0.취소) >'))
        if p_select == 0:
            break
        elif p_select == 1:
            print('-'*50) 
            print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
            print('-'*50) 
            for s_dic in students:   
                for d_key in s_dic:
                    print(s_dic[d_key],end='\t')  
                print()
            print('-'*50)
        print() 
                   
    elif choice == 3:
        print('학생검색을 선택하셨습니다.')
        s_name = input('검색하고자 하는 학생의 이름을 입력하세요 (0. 취소)>')
        if s_name == '0':
            break
        for i, s_dic in enumerate(students):
            if s_name == s_dic['name']:  
                print('{}학생의 이름이 존재합니다.'.format(s_name))
                print('{},{}'.format(i+1,s_name))   
        
        
    elif choice == 4:  
        while True:
            print('학생성적수정을 선택하셨습니다.')
            s_title= ['','국어','영어','수학']
            s_name = input('수정하고자 하는 학생의 이름을 입력하세요 (0. 취소)>')   
            chk = 0                                                             
            if s_name == '0':                                                
                break
            for s_dic in students:                                            
                if s_name == s_dic['name']: 
                    break
                chk += 1
            if chk == len(students) :                                   
                print('{}학생의 이름이 존재하지 않습니다. 다시입력하세요'.format(s_name))
            else:
                print('학생의 이름이 존재합니다')
                print('학생의 성적이 존재하는 위치는 {}'.format(chk))
                while True:
                    c_sub = int(input('수정하고자 하는 과목을 입력하세요 (1. 국어 2. 영어 3. 수학 0. 취소) >>'))  
                    s_1 = 'kor'
                    s_2 = 'eng'
                    s_3 = 'math'
                    if c_sub == 0:
                        break
                    elif c_sub == 1 :
                        print('국어를 선택하셨습니다.')
                        print('현재 {}의 {} 성적 : {}'.format(s_name,s_title[c_sub],students[chk][s_1]))
                        c_kor = int(input('수정할 {}성적을 입력하세요 >'.format(s_title[c_sub])))
                        s_dic[s_1] = c_kor
                        s_dic['total'] = s_dic[s_1] + s_dic[s_2] + s_dic[s_3]   
                        s_dic['avg'] = float('{:.2f}'.format(s_dic['total']/3))
                        print(s_dic)
                        print(students)
                    elif c_sub == 2 :
                        print('영어를 선택하셨습니다.')
                        c_eng = int(input('수정할 영어성적의 성적을 입력하세요 >'))
                        s_dic['eng'] = c_eng
                        s_dic['total'] = s_dic[s_1] + s_dic[s_2] + s_dic[s_3]   
                        s_dic['avg'] = float('{:.2f}'.format(s_dic['total']/3))
                        print(s_dic)
                        print(students)
                    elif c_sub == 3 :
                        print('수학을 선택하셨습니다.')
                        c_math = int(input('수정할 수학성적의 성적을 입력하세요 >'))
                        s_dic['math'] = c_math
                        s_dic['total'] = s_dic[s_1] + s_dic[s_2] + s_dic[s_3]   
                        s_dic['avg'] = float('{:.2f}'.format(s_dic['total']/3))
                        print(s_dic)
                        print(students)
    
    elif choice == 5:     # => 띄어쓰기
        print('등수처리를 선택하셨습니다.')

        for i, s_dic in enumerate(students): 
            s_rank = 1     # => 이 숫자의 위치
            for c_total in students:
                if s_dic['total'] < c_total['total']:
                    s_rank += 1
            s_dic['rank'] = s_rank
        print(students)

        
    elif choice == 6:
        print('학생삭제를 선택하셨습니다.')
        chk = 0   
        while True:
            s_name = input('수정하고자 하는 학생의 이름을 입력하세요 (0. 취소)>')
            if s_name == '0':
                break
            for s_dic in students:
                if s_name == s_dic['name']:
                    print('{}학생의 이름이 존재합니다.'.format(s_name))
                    break
                else:
                    print('찾고자 하는 학생이 없습니다')
                    break    
            chk += 1
            if chk == len(students):
                break
            
            else:                
                print('학생의 성적이 존재하는 위치는 {}'.format(students[chk]))
                d_select = input('삭제를 선택하시겠습니까?(1. 삭제  0. 취소)>')
                if d_select == '1' :
                    del students[chk]
                    print('삭제되었습니다')
                    print(students)
                elif d_select == 0 :
                    break                    
        
    elif choice == 0:
        print('프로그램을 종료합니다')
        break
    
