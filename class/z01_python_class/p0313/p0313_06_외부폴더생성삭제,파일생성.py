import os

print('현재 운영체제 :', os.name)
print('현재 폴더 :', os.getcwd())
print('현재 폴더내 파일들 표시:', os.listdir())      # 디렉토리


# 폴더 생성
os.mkdir('hello')  # mkdir: make directory    # 현재 폴더 : C:\workspace\medical1

# 폴더 삭제
os.rmdir('hello')


# 폴더가 존재하는지 확인
if not os.path.exists(''):       # 존재하는지 여부 확인
    os.mkdir("hello")
else:
    os.rmdir("hello")


# 파일 생성
with open('students.txt','w') as f:
    f.write("1,'홍길동',100,99,87,286,95.33,2")
 
str1 = "1, '홍길동', 100, 99, 87, 286, 95.33, 2"
s_list = str1.split(',')

for i in s_list:
    print(i)
    
    
    
# clear