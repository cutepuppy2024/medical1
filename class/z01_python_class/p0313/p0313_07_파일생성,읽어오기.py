import os


# 1. 파일 생성
f = open ('students.txt','w',encoding='utf-8')
f.write("1,'홍길동',100,99,87,286,95.33,2,\n")
f.write("2,'유관순',98,93,87,278,92.67,3")
f.close()   # 파일닫기

# # 2. 파일 생성 - with 사용하면 f.close() 사용하지 않아도 됨.
with open('students1.txt',"w") as f:
    f.write("1,'홍길동',100,99,87,286,95.33,2")
    
# 파일 읽기
t_list = []
out_f = open("students.txt","r",encoding='utf-8')
while True :
    txt = out_f.readline()   # 1줄씩 읽어오기
    # print(type(txt))
    if txt == "" :
        break
    print(txt,end='')
    t_list.append(txt)
print()   
print(t_list)
out_f.close()   # 꼭 닫아주어야 한다




# 파일 삭제
os.remove('students.txt')


# clear