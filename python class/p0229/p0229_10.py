
# while True:
#     n = int(input('원하는 번호를 입력해주세요 >>'))
    
#     # n은 문자열
# # print(n)
#     if n.isdigit(): # 숫자지만 문자열 3x) "0" '1'
#     n = int(n)
#     else:
#         print('문자가 입력되었습니다. 다시입력해주세요')
 
# str1 = '10'
# print(str1.isdigit()) #True

# str2 = 'a'
# print(str2.isdigit())  #False

# While True:
#     n = input("원하는 번호를 입력해주세요")
    
    
# 이름을 검색해보고, 이름을 검색해서 삭제

students = [[1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],[4,'김유신', 70], [5,'김구',95]]

while True:
    print('1. 학생 검색')
    print('2. 학생 삭제')
    print('3. 프로그램종료')
    ch = input('원하는 번호를 입력해주세요 >>')
    if ch.isdigit():  # 입력한게 숫자면 True # 문자열만 인식한다!!! 위에 int를 쓰면 안됨 !!
        ch = int(ch)
    
    if ch == 1:
        searchName = input('검색할 학생의 이름을 입력해주세요 >>')
        chk = 0
        for stu in students:
            # print(stu)
            if searchName in stu:
                print('있음,{}학생이 존재합니다'.format(searchName))
                print(stu)
                chk = 1  # 학생이 존재하면 chk값이 변한다는 의미
        if chk == 0: # 학생이 존재하지 않음
            print('검색하신 학생이 존재하지 않습니다')
            # else:
            #     print('존재하지 않습니다')

    elif ch==2 :
        delName = input('삭제하고 싶은 학생의 이름을 입력하세요 >>')
        c1 = 0
        for i, stu in enumerate(students): # students 리스트안에 있는 원소 stu를 반복, index : 0부터시작 할것이다
            if delName in stu:
                del(students[i])
                c1 = 1
                print(delName,'학생이 삭제되었습니다')
        if c1 == 0:
            print('삭제하실 학생의 이름이 존재하지 않습니다')
        print(students)
        
    elif ch ==3 :
        print('프로그램이 종료되었습니다')
        break
    else: 
        print('잘못입력하셨습니다. 다시 입력해주세요')
    