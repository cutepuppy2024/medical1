students = []
stu_num = 0
while True :
    print('='*40)
    print('[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적전체출력') # 국, 영, 수 점수를 수정해 볼 수 있음. (유의: 국어를 바꾸면, 합, 평균)
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')  
    print('6. 학생정렬')
    print('0. 프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요>>')
    if not choice.isdigit():
        print('숫자를 입력하세요')
        continue
    choice = int(choice)
    
    if choice == 1 :
        print('학생성적입력을 선택하셨습니다')
        while True :
            name = input('학생 이름을 입력하세요(-1.종료)>>')
            if name == '-1':
                break
            stu_num += 1
            kor = int(input('국어성적 >>'))
            eng = int(input('영어성적 >>'))
            math = int(input('수학성적 >>'))
            total = kor + eng + math
            avg = '{:.2f}'.format(total/3) 
            stu = [stu_num,name,kor,eng,math,total,avg,1]
            students.append(stu)
            print(students)
        
    elif choice == 2 :
        print('학생성적전체출력을 선택하셨습니다')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*50)
        for i in students:
            for j in i:
                print(j,end='\t')
            print()
        print('-'*40)
        
    elif choice == 3 :
        print('학생검색을 선택하셨습니다')
        search_Name = input('검색하고자 하는 학생의 이름을 입력하세요(0.중단) >>')
        chk = 0
        if search_Name == '0':
            break
        for i in students:
            if i[1] == search_Name:
                print('{},학생이 명단에 있습니다'.format(search_Name))  
                chk = 1
                break
            else:
                print('{},학생이 명단에 없습니다.'.format(search_Name))
                print('다시 입력해 주세요')
                break
                
    elif choice == 4 :   
        while True :
            print('학생수정을 선택하셨습니다')
            chk = 0
            count = 0
            search_Name = input('수정하고자 하는 학생의 이름을 입력하세요(0.중단) >>')
            if search_Name == '0':
                break
            for stu in students:
                if search_Name == stu[1]:                    
                    print('{},학생이 명단에 있습니다'.format(search_Name))  
                    chk = 1
                    break
                count += 1

            if chk == 1:
                cor_sub = input('수정하고자 하는 과목을 선택해 주세요(1.국어 2.영어 3.수학 0.취소)>>')
                if cor_sub == '0':
                    break  
                cor_sub = int(cor_sub)                 
                if cor_sub == 1:
                    print('국어를 선택하셨습니다')
                    print('{}의 국어 성적은 현재 {}점 입니다'.format(search_Name,students[count][2]))
                    c_kor = int(input('수정할 국어성적을 입력하세요 >>'))
                    students[count][2] = c_kor
                    print('{} 학생의 국어 성적이 {}점으로 수정되었습니다.'.format(search_Name,students[count][2]))
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]  
                    students[count][6] = (students[count][2]+students[count][3]+students[count][4])/3 
                    print(students[count])
                elif cor_sub == 2:
                    print('영어를 선택하셨습니다')
                    print('{}의 영어 성적은 현재 {}점 입니다'.format(search_Name,students[count][3]))
                    c_eng = int(input('수정할 영어성적을 입력하세요 >>'))
                    students[count][2] = c_eng
                    print('{} 학생의 영어 성적이 {}점으로 수정되었습니다.'.format(search_Name,students[count][3]))
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]  
                    students[count][6] = (students[count][2]+students[count][3]+students[count][4])/3 
                    print(students[count]) 
                if cor_sub == 3:
                    print('수학을 선택하셨습니다')
                    print('{}의 수학 성적은 현재 {}점 입니다'.format(search_Name,students[count][4]))
                    c_kor = int(input('수정할 수학성적을 입력하세요 >>'))
                    students[count][2] = c_eng
                    print('{} 학생의 수학 성적이 {}점으로 수정되었습니다.'.format(search_Name,students[count][4]))
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]  
                    students[count][6] = (students[count][2]+students[count][3]+students[count][4])/3 
                    print(students[count]) 
            else:
                print('찾는 학생이 존재하지 않습니다')                                                              

        
                
                          
        
            