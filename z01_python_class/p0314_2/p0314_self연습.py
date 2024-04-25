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
            content = f.readline()
            if content == '' : break
            print(content,end='\t')
            
        f.close()
    
    elif choice == 3:
        print("3. 파일 저장하기")
        p_file = input("저장할 파일의 위치를 선택하세요 (1. 기존파일  2. 새로운파일) >>")
        if p_file == '1':
            os.listdir()
            for f_name in os.listdir():
                if f_name.endswith('.txt'):
                    print(f_name)

            s_name = input('저장할 파일명을 입력하세요 >>')

            f = open(s_name,'a',encoding='utf-8')

            while True:
                txt_input = input('내용을 입력하세요(-1: 취소) >')
                if txt_input == '-1':
                    break
                f.write(txt_input+'\n')
            print(txt_input)

            f.close()

        elif p_file == '2':
            n_name = input("새로만들 파일명을 입력하세요>")

            f = open(n_name,'w',encoding='utf8')

            while True:
                txt_input = input('내용을 입력하세요(-1:취소) >>')
                if txt_input == '-1':
                    break
                f.write(txt_input+'\n')

            f.close()


# .txt 파일 내용을 읽어와서 
# .txt에 그 내용을 추가해 보세요
            
f = open('memo.txt','r',encoding='utf8')
ff = open('memo1.txt','a',encoding='utf8')

while True:
    content = f.readline()
    if content == '' :
        break
    ff.write(content)

f.close()

fff = open('memo1.txt','r',encoding='utf8')

while True:
    content1 = fff.readline()
    if content1.strip() == '': break
    print(content1,end='\n')

fff.close
