# readline : 1 줄을 str타입으로 가져옴

f = open("str.txt","r",encoding='utf8')
while True:
    txt = f.readline()
    if txt == " ": break   
    print(txt)
f.close()  
print("모든 파일을 읽어 왔습니다")



# readlines : 1줄씩 리스트타입으로 저장
f = open("str.txt", "r", encoding='utf8')
txt_list = f.readlines()
txt = f.readlines()
print(txt)


# 파일 확인
import os
if os.path.exists("str.txt"):
# f = open("str.txt", "r", encoding='utf8')
    with open("str.txt",'r', encoding='utf8') as f: # 변수명을 뒤에 씀
        txt_list = f.readlines()    # ['안녕하세요. 반갑습니다.\n', '저는 홍길동입니다.\n', '파이썬 수업을 열심히 듣고 있습니다.\n']
        print(txt_list)
        
        for txt in txt_list:
            print(txt,end='')
        print()

else:
    print('파일이 존재하지 않습니다')

# < 정리 >
# 1. 파일 열기
# 2. 파일 읽기
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴
# 3. 파일 닫기


    


# clear

