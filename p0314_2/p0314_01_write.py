# < 파일 입출력 >
# r = 읽기, w = 쓰기, r+ = 읽기/쓰기,  a = 쓰기모드, 이어서,  t = 텍스트모드, b = 이진모드, 이진파일


# 파일열기
file = open("memo.txt","w",encoding='utf-8')

# 파일쓰기
print(' [ 메모장 실행 ]')
print('-'*40)
while True:
    txt = input()
    if txt == '0' :
        print('메모장을 저장합니다')
        break
    print(txt)
    file.write(txt+"\n")

# 파일닫기
file.close()

print("파일이 저장되었습니다")




# 파일열기
file = open("memo1.txt","w",encoding='utf-8')

# print(' [ 메모장 실행 ]')
print('-'*40)
while True:
    txt = input()
    if txt == '0' :
        print('메모장을 저장합니다')
        break
    print(txt)
    file.write(txt+"\n")

# 파일닫기
file.close()

print("파일이 저장되었습니다")




# 파일열기
file = open("memo2.txt","w",encoding='utf-8')

# 학생성적 
print('학생성적입력')
print('-'*40)
while True:
    txt = input()
    if txt == '0' :
        print('메모장을 저장합니다')
        break
    print(txt)
    file.write(txt+"\n")

# 파일닫기
file.close()

print("파일이 저장되었습니다")


# clear


