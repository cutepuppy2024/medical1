import os

while True:
    print('[윈도우 탐색기]')
    print("-"*40)
    print("1. 폴더 내 파일 확인")
    print("2. 파일 불러오기")
    print("3. 파일 저장하기")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요 >>"))
    
    if choice == 1:
        print("1. 폴더 내 파일 확인하기")
        os.listdir()
        print(os.listdir())  # 리스트형태로 출력됨
        for f_name in os.listdir():
            if f_name.endswith('.txt'):
                print(f_name)
              
    elif choice == 2:
        print("2. 파일 불러오기")
        os.listdir()
        print(os.listdir())  
        for f_name in os.listdir():
            if f_name.endswith('.txt'):
                print(f_name)
        s_file = input('불러올 파일명을 입력하세요 >>')
        
        f = open(s_file,'r',encoding='utf8')
        
        while True:
            content = f.readline
            if content == '' : break
            print(content)
            
        f.close()
        
    elif choice == 3:
        print("3. 파일 저장하기")
