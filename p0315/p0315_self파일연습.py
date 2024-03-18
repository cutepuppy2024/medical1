# 학생성적파일, 학생성적코멘트 파일을 만들고, 코멘트 파일의 내용을 성적파일에 붙이기
f =  open("students.txt",'w',encoding='utf8')

while True:
    txt_input = input('학생성적을 입력하세요(-1: 취소) >')
    if txt_input == '-1': break
    f.write(txt_input)
print()
    
f.close()

ff = open("student1.txt",'w',encoding='utf8')

while True:
    txt_input = input('성적코멘트 입력 (-1: 취소)')
    if txt_input == '-1': break
    ff.write(txt_input)
print()

ff.close()

ff = open('student1.txt','r',encoding='utf8')  # 코멘트파일 읽기
f = open('students.txt','a',encoding='utf8')  # 성적파일에 붙여넣기

while True:
    content = ff.readline()   # 코멘트 파일
    if content == '': break
    f.write(content)

ff.close()
f.close() 


chk = open('students.txt','r',encoding='utf8') 

while True:
    c_content = chk.readline()
    if c_content == '':
        break
    print(c_content,end='\n')
    
chk.close()  

# clear