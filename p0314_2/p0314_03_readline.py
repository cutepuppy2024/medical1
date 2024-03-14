# 파일저장
file = open("str.txt","w",encoding='utf8')

file.write("안녕하세요. 반갑습니다.\n")
file.write("저는 홍길동입니다.\n")
file.write("파이썬 수업을 열심히 듣고 있습니다.\n")

file.close()
print('파일이 저장되었습니다')


# 파일 읽어오기
file = open("str.txt",'r',encoding='utf8')
while True:
    txt = file.readline()   # 파일 1줄 읽어오기
    if txt == '':
        break
    print(txt,end='')

# file.close()
file = open("stu.txt",'w',encoding='utf8')

file.write('1, 홍길동,100,100,100,300,100.0')

file.close()

# stu.txt 파일을 출력하시오
file = open("stu.txt",'r',encoding='utf8')

s_list = []
while True:
    txt= file.readline()
    print(txt)
    if txt == '':
        break
    
    s_list = txt.split(',')      #=> 리스트타입으로 변환, 문자를 하나씩 끊으면서 리스트에 들어감
    s_list[0]  =int(s_list[0].strip())     
    s_list[1]  =s_list[1].strip()
    s_list[2]  =int(s_list[2].strip())
    s_list[3]  =int(s_list[3].strip()) 
    s_list[4]  =int(s_list[4].strip())
    s_list[5]  =int(s_list[5].strip()) 
    s_list[6]  =float(s_list[6].strip())             
    print(s_list)

file.close()



# clear