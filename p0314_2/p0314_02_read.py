


# 파일열기
file = open("stu.txt",'r',encoding='utf8')


# 파일읽기
content = file.read() # 메모장에 있는 모든 글을 읽어옴.
content = content.strip()  # 문자열 빈공백제거 strip
# 1, 홍길동, 100,100,99  split(',') : 문자열을 쉼표로 분리 -> list

# content = content.split(',')
stuNo, name, kor, eng, math, total, avg = content.split(',')

c_list = [0]*7
c_list[0] = int(stuNo)
c_list[1] = name
c_list[2] = kor
c_list[3] = eng
c_list[4] = math
c_list[5] = total
c_list[6] = avg
print(c_list)

# 파일닫기
file.close()





# clear


