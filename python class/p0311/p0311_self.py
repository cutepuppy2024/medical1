# 학생성적처리시스템 함수를 사용하여 구현하기
from  score import*

students = []   # 딕셔너리형태로 학생입력하기
cnt = 0
s_title = ['', '국어', '영어', '수학']
while True:
    print('[학생성적처리시스템]')
    print('-'*50)    
    print('1. 학생성적입력') 
    print('2. 학생성적전체출력') 
    print('3. 학생검색')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 등수처리') 
    print('0. 프로그램종료')
    print('-'*50)     
    
    choice = input('원하는 작업을 선택하세요 >')
    if not choice.isdigit():
        print('숫자를 입력하세요')
        break
    choice = int(choice)

    if choice == 1:
        print('학생성적입력을 선택하셨습니다.')
        while True:        
            stu = {}
            name = input('이름을 입력하세요 (0.취소) >')
            if name == '0':
                break
            stu_input(cnt,stu,name,s_title,students)
         
    elif choice == 2:
        print('학생성적전체출력을 선택하셨습니다.')
        p_sel = int(input('출력하시겠습니까?(1.출력 0.취소)'))
        if p_sel == 0:
            break
        all_p(students)

    elif choice == 3:
        print('학생검색을 선택하셨습니다')
        chk = 0
        s_name = input('검색하고자 하는 학생의 이름을 입력하세요 (0.취소)')
        if s_name == 0:
            print('검색을 취소하셨습니다.')
            break
        search_N(chk,cnt,s_name,students)

    elif choice == 4:
        pass  
    elif choice == 5:
        pass  
    elif choice == 0:
        print('프로그램을 종료합니다')
        break 
 
   