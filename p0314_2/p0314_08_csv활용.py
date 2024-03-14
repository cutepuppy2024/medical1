# medical_1.csv 파일을 읽어와서 출력하시오

# 파일열기
f = open("medical_1.csv",'r',encoding='utf8')


# 파일읽기
cnt = 0
sum = 0

while True:
    content = f.readline()
    if cnt == 0:     # 첫줄 삭제
        cnt += 1
        continue
    if content == '' : break
    # print(content,end='')
    # 리스트에 넣기
    s_list = content.split(',')
    # print(s_list)     => 공백은 들어감
    print(s_list,len(s_list))
    s_list[1] = int(s_list[1])
    sum += s_list[1]       
print(sum)
        

    
# 파일닫기
f.close()



    