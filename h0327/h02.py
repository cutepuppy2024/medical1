# 파일을 읽어와서 출력하시오

# with open("member.csv","r",encoding='utf8') as f:
#     while True:        
#         txt = f.readline()
#         if txt == '': break
#         txt_list = txt.split(",")
#         print(txt_list[1])   # 아이디만 출력

# 파일열기
# 상대경로: medical1 폴더안 member.csv - 현재 폴더 기준
# medical1>h0327>aaa  폴더안 h0327/aaa.member2.csv    
# 절대경로: c:/workspace/medical1/h0327/aaa.member2.csv 
with open("h0327/aaa/member2.csv","r",encoding='utf8') as f: # 절대경로
    while True:        
        txt = f.readline()
        if txt == '': break
        mem = txt.split(",")
        print(mem[0], mem[1])   # 아이디만 출력
        
        
        #상위폴더부터 찾기 시작한다면 아까는 medical1 하위 폴더에 있었는데 왜 안 됐을까?