# str.txt 파일의 내용을 모두 출력하시오
with open('str.txt','w',encoding='utf8') as f:
    f.write("파이썬 화이팅")

with open('str1.txt','w',encoding='utf8') as f:
    f.write('잘한다')


f = open("str.txt",'r',encoding='utf8')

while True:
    txt = f.readline()
    if txt.strip() == '':     # 공백제거
        break
    print(txt,end='')
print()

f.close()

print('-'*50)
# str.txt 파일 내용을 읽어와서 
# str1.txt에 그 내용을 추가해 보세요


f = open("str.txt",'r',encoding='utf8')
ff = open("str1.txt",'a',encoding='utf8')

while True:
    cont = f.readline()   # 파일 내용을 읽어오기  : 파이썬 화이팅
    if cont.strip() =='': break
    ff.write(cont)        # 파일 내용을 추가하기  
f.close()
ff.close()

fff = open('str1.txt','r',encoding='utf-8')
while True:
    cont1 = fff.readline()
    if cont1.strip() == "": break
    print(cont1,end="\n")  # str1에 추가되어 있어야 함
    
fff.close()


# clear