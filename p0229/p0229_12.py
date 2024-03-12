member = []

# for i in range(10):
cnt = 0
# 이름을 입력받아서 [[1, 홍길동],[2,유관순],[3,이순신]]   
while True:
    print('-'*25)
    print('1. 입력')
    print('2. 출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch = input('원하는 번호를 선택하세요 >>')
    print('-'*25)
    ch = int(ch)
    if ch == 1:
        print('입력')
        name = input('이름을 입력해주세요 >>> ')
        cnt = cnt + 1
        m = [cnt, name]
        member.append(m)
        print(member)

    elif ch == 2 :
        print('출력') 
        print(member)
        print('번호\t이름')
        print('-'*20)
        for i in range(len(member)):   # while 을 쓴다면?
            # print(member[i]) 
            print('{}\t{}'.format(member[i][0],member[i][1]))
            i += 1
        
    elif ch == 3 :
        chk = 0
        search_Name = input('검색할 이름을 입력하세요 >>')
        for s, stu in enumerate(member):       
            if search_Name in stu:
                print(search_Name,'이 존재합니다')
                print(s,search_Name)
                chk = 1
        if chk == 0:
            print('검색하신 학생의 이름이 존재하지 않습니다')
            
    elif ch == 4 :
        delName = input('삭제할 이름을 입력하세요 >>')
        for i, s_del in enumerate(member):
            if delName in s_del:
                print(delName,'이 존재합니다')
                del(member[i])
                print(delName,'이 삭제되었습니다')
                print(member)      
                s1 = 1     
                   
    elif ch == 5 :
        print('수정입니다')                 # 코드가 길어질수록 코드를 잘 알아볼 수 있게 만들어야한다
        # 누구의 정보를 수정할지 > 누구의 정보를 수정하시겠습니까?
        # 번호, 이름(현재 있는 정보) > 중에 어떤 것을 수정할지
         # 만약 번호를 수정한다면 -> 수정될 값 1 -> 6
         # 만약 이름을 수정한다면 -> 수정될 값 홍길동 > 홍길자
        reName = input('수정하고 싶은 학생의 이름을 입력해주세요 >>')        
        for q, cor in enumerate(member):
            if reName in cor :  # 존재한다면
                print(reName,'님을 선택하셨습니다.')
                ch_num= input('수정하고 싶은 항목을 선택해 주세요(1.번호수정, 2.이름수정)')
                if ch_num == '1':
                    print(reName,'님의 번호 수정을 선택하셨습니다')
                    print(reName,'님의 번호는',member[i][0],'입니다')
                    stu_num = input('새로운 번호를 입력해주세요 >>')
                    stu_num = int(stu_num)
                    member[i][0] = stu_num
                elif ch_num == '2':
                    print(reName,'님의 이름 수정을 선택하셨습니다')
                    print(reName,'님의 이름은',member[i][1],'입니다')
                    stu_name = input('변경할 이름을 입력해주세요 >>')
                    member[i][1] = stu_name
                
                
                else:
                    print('잘못입력하셨습니다')
                    break
                
    else:
        print('다시입력')


