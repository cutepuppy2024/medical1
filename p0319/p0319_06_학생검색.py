stu = [
    ["홍길동",100],
    ["유관순",98],
    ["이순신",100],
    ["김구",50],
    ["강감찬",99],
    ["김유신",90],
    ["홍길순",80],
    ["홍길자",70]
]

# 이름으로 검색, 홍이 들어가는 사람을 모두 검색해서 출력하시오

while True:
    print('[학생성적 검색]')
    print('1. 이름으로 검색')
    print('2. 점수 검색')
    print('3. 학생성적검색')
    choice = int(input("원하는 번호를 입력하세요. >>"))

    if choice == 1 :
        search_list = [] # 검색된 사람의 이름이 저장
        search = input('검색하고자 하는 단어를 입력하세요 >>')
        cnt = 0
        for s in stu:
            # if n.find(search) != -1:  # 검색어가 포함이 되어 있는지 확인
            if search in s[0]:
                search_list.append(cnt)
            cnt += 1  
            
        if len(search_list) == 0:
            print('찾고자 하는 사람이 없습니다')
        
        else:
            print(f'{search}으로 검색된 사람',end ='')
            for i in search_list:
                print(stu[i][0],end='')
                print()      
                
    elif choice == 2 :  
        # 80 -> 80점 이상인 사람의 이름이 출력되도록 해보세요
        score = int(input("검색하고자 하는 점수를 입력하세요 >>"))
        score_list = []
        cnt = 0
        for s in stu:
            if score <= s[1]:
                score_list.append(cnt)
        cnt += 1
        
        if len(score_list) == 0:
            print(f'{score} 이상인 사람이 없습니다')
            
        else:
            print(f'{score} 이상인 사람 ',end ='')  # 상관없음
            for i in score_list:
                print(stu[i][0],stu[i][1])
            print()
            print()
            
    elif choice == 3:
        while True:
            print(" [ 1. 학생 이름으로 검색 ]")
            print(" [ 2. 점수이상 검색 ]")
            print(" [ 3. 점수이하 검색 ]")
            print(" [ 0. 이전화면 이동 ] ")
            
            choice = int(input("원하는 번호를 입력하세요.>>"))
            
            if choice == 1:       
                search = input("찾고자 하는 학생 이름을 입력하세요. >>")
                s_list= []
                # 전체리스트에서 학생 검색
                s_cnt = 0
                for i in stu:
                    if i.name.find(search) != -1:
                        s_list.append(i)
                        print(i)                          
                if s_cnt == len(stu):
                    print("찾고자 하는 학생이 없습니다. 다시 검색하세요")              
                else:
                    print(stu[s_cnt]) 

            elif choice == 2:
                pass
            elif choice == 3:
                pass
                
        
            
            
