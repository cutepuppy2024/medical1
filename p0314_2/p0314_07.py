# str.txt 파일의 내용을 모두 출력하시오



f = open("str.txt",'r',encoding='utf8')

while True:
    txt = f.readline()
    if txt.strip() == '':     # 공백제거
        break
    print(txt,end='')

f.close()


# str.txt 파일 내용을 읽어와서 
# str1.txt에 그 내용을 추가해 보세요


f = open("str.txt",'w',encoding='utf8')
ff = open("str1.txt",'a',encoding='utf8')

while True:
    txt = f.readline()   # 파일 내용을 읽어오기
    if txt.strip() =='': break
    ff.write(txt)        # 파일 내용을 추가하기  
f.close()
ff.close()

fff = open('str1.txt','r',encoding='utf-8')
while True:
    txt = f.readline()
    if txt.strip() == "": break
    print(txt,end="")
    
fff.close()