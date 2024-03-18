in_file = None
out_file = None

# 파일열기 
in_file = open("C:/workspace/medical1/jk.jpg","rb")
out_file = open("c:/a/aa.jpg","wb")  # a 라는폴더에 저장되어 있음

in_file = open("C:/workspace/medical1/mem.txt","rb")
out_file = open("c:/a/aaaa.txt","wb") 

# 파일읽기, 쓰기
while True:
    bin = in_file.read(1)    # 1의 의미 :  파일을 나눌 때는 1byte씩 바이너리로 잘라서 패킷을 복사
    if not bin: break
    out_file.write(bin)

# 파일 닫기  
in_file.close()
out_file.close()
print('복사가 완료되었습니다.')