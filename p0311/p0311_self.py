# 4. 학생성적
students = []   # 딕셔너리형태로 학생입력하기
cnt = 0
while True:
    print('[학생성적처리시스템]')
    print('-'*50)    
    print('1. 학생성적입력') 
    print('2. 학생성적전체출력') 
    print('3. 학생성적수정')
    print('4. 학생성적삭제')
    print('5. 등수처리') 
    print('0. 프로그램종료')
    print('-'*50)     
    
    choice = input('원하는 작업을 선택하세요 >')
    if not choice.isdigit():
        print('숫자를 입력하세요')
        break
    choice = int(choice)

    if choice == 1:
        print('학생성적입력을 선택하셨습니다.')
         
          
    elif choice == 2:
        pass  
    elif choice == 3:
        pass  
    elif choice == 4:
        pass  
    elif choice == 5:
        pass  
    elif choice == 0:
        print('프로그램을 종료합니다')
        break 
 
   