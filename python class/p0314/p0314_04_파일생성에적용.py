# 파일 1개 저장

# file open
file = open("memo.txt",'w',encoding='utf8')
try:
    # file write
    file.write('안녕하세요1.\n')
    file.write('안녕하세요2.\n')
    file.write('안녕하세요3.\n')
    # print(1/0)
    file.write('안녕하세요4.\n')
except:
    print('저장시 에러가 났습니다')
finally:
    # 파일닫기
    file.close()   #예외발생해도, 예외발생하지 않아도 무조건 실행
    
 #----------------------------------------------------------------------   
 
file = open("memo.txt",'w',encoding='utf8')
try:
    # file write
    file.write('안녕하세요1.\n')
    file.write('안녕하세요2.\n')
    file.write('안녕하세요3.\n')
    print(1/0)
    file.write('안녕하세요4.\n')
except Exception as e:     # 어떤에러가 났는지 설명해줌
    print('저장시 에러가 났습니다')
    print(e)
finally:
    # 파일닫기
    file.close()   #예외발생해도, 예외발생하지 않아도 무조건 실행   




# clear