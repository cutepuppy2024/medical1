# 변수 - 1개의 데이터 / 리스트 - 여러개 / 디셔너리, 토플 => 여러개
# 변수종류 - bool, str, int, float  => Database program은 bool 빼고 사용, 명확히 알고 어떤 Data를 넣을지 판단한 후 input해야함!! 
# ex) 지마켓 입력창 : 수량 / Data가 숫자가 아니면 오류 => 숫자만 들어갈 수 있도록 제한을 걸어주는 것임
#                    로그인 / 아이디 - => error가 나지 않도록 하는 것이 내가 할 일, 어떤 식으로 입력을 받을것인지 디자인

# students = [] # 학생성적저장  => 항상 주석을 달아놓는 것이 좋다, 이직이 많고 담당자 변할 수 있어서  # java에서는 class  사용/ python과 다른것 구분하기 !!
students = [
    [1, '홍길동', 100, 100, 99, 299, 96.67,1],
    [2, '유관순', 99, 99, 98, 296, 98.67,1], 
    [3, '강감찬', 80, 80, 81, 241, 80.33,1],
    [4, '김구', 100, 100, 90, 290, 96.67,1],
    [5, '김유신', 90, 70, 50, 210, 70.0,1],
    [6, '이순신', 100, 100, 100, 300, 300.0,1]
]
cnt = len(students) # 학번사용
while True :
    print('='*40)
    print('[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적전체출력') # 국, 영, 수 점수를 수정해 볼 수 있음. (유의: 국어를 바꾸면, 합, 평균)
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')  
    print('6. 학생삭제')
    print('0. 프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >>')  # 변수 정의를 오류가 날 것을 고려해서 내려 주어야 하는듯!!
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
        continue # 반복문 다시 실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1:                #데이터 하나가 바뀌었을 때 영향받는 데이터 전체 수정 유의!!!
        # 무한반복
        while True :  # 입력을 계속반복하고자 할때 묶어준다
            print('학생성적을 입력합니다')
            print('-'*10)
            student = [] # 초기화
            name = input('이름을 입력하세요 (-1. 취소)>>')
            if name == '-1' :  # while True를 빠져나와 그 위의 루프를 돈다
                break
            # kor = int(input('국어성적을 입력하세요 >>'))
            # eng = int(input('영어성적을 입력하세요 >>'))
            # math = int(input('수학성적을 입력하세요 >>'))
            cnt += 1  # 학번
            student.append(cnt)
            student.append(name)
            student.append(int(input('국어성적을 입력하세요 >>')))   
            student.append(int(input('영어성적을 입력하세요 >>')))
            student.append(int(input('수학성적을 입력하세요 >>')))
            sum = student[2] +student[3] + student[4]
            # 합계저장
            student.append(sum) 
            # 평균저장
            student.append("{:.2f}".format(sum/3))
            students.append(student)
            # 전체출력
            print(students)
    
    # 2. 학생성적전체출력
    elif choice == 2:
        print('[학생성적 출력]')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        #2차원 리스트는 for문을 2번 사용함    
        for stu in students:                                      
            for s in stu:
                print(s, end='\t')                               
            print()
        print('-'*50)
        
    #3. 학생성적검색
    elif choice == 3:
        # 찾고자 하는 학생찾기
        while True:
            # 멈춤
            search = input('검색하고 싶은 학생의 이름을 입력하세요 .(0.취소)>>')
            chk = 0 # 찾는 정보확인
            count = 0
            if search == "0":
                break
            for stu in students :
                if search in stu:
                    chk = 1 # 찾는 정보확인
                    break
                count += 1 # 못찾았을 때 반복되면서 +1, for 구문 반복
            if(chk==1):
                # 전체학생 정보출력
                print('[학생성적 출력]')
                print('{}의 학생정보를 찾았습니다'.format(search))
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                print('-'*50)
                for i in students[count] :
                    print(i,end='\t' )
                print()
            else:
                print('찾는 학생 정보가 없습니다')
                
    # 4. 학생성적 변경
    elif choice == 4:
        while True :
            search = input('찾는 학생의 이름을 입력하세요 >>(0.취소)')
            if search == "0":
                break
            chk = 0
            count = 0
            for stu in students:
                if search in stu :
                    chk = 1
                    break
                count += 1  # 찾는 학생의 위치값
            if chk == 0 :
                print('찾는 학생의 정보가 없습니다')
            else :
                print('입력한 학생을 찾았습니다')
                print('[변경할 과목 선택]')
                print('1.국어 2.영어 3.수학')
                print('-'*20)
                num = int(input('숫자를 입력하세요>>'))
                
                if num == 1 :
                    print('국어를 선택하셨습니다')
                    print('현재 국어점수:',students[count][2])
                    num = int(input('변경점수를 입력하세요'))
                    students[count][2] = num
                    #합계,평균도 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = students[count][5]/3
                    #출력
                    print(students)
                    
                elif num ==2 :
                    print('영어를 선택하셨습니다')
                    print('현재 영어점수:',students[count][3])
                    num = int(input('변경점수를 입력하세요'))
                    students[count][3] = num
                    #합계,평균도 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = students[count][5]/3
                    #출력
                    print(students)
                elif num == 3: 
                    print('수학을 선택하셨습니다')
                    print('현재 영어점수:',students[count][4])
                    num = int(input('변경점수를 입력하세요'))
                    students[count][4] = num
                    #합계,평균도 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                    students[count][6] = float("{:.2f}".format(students[count][5]/3)) #"{:.2f}".format(students[count][5]/3)  
                    #출력
                    print(students)
                    
                else :
                    print('성적 취소를 선택하셨습니다')
    # 5. 등수처리
    elif choice == 5 :
        while True:
            choice = input('등수처리를 실행하시겠습니까?(1.실행 0.취소)')
            if choice == '0':
                print("등수처리를 취소하셨습니다")
                break
            else:
                # 등수처리 진행
                for i_stu in students:
                    no = 1
                    for j_stu in students:
                        # 각각의 총합 비교
                        if i_stu[5] < j_stu[5]:      # 비교대상을 좁혀주기
                            no += 1  # 비교대상 총합이 더 크면 1 증가
                            i_stu[7] = no  #등수위치에 no 저장                    
            print('등수처리가 완료되었습니다')
            print('-'*40)
            print('[등수확인]') 
            print(students)       
            
    # 6. 학생삭제
    elif choice == 6 :
        while True:
            search = input('삭제하려는 학생의 이름을 입력하세요>>')
            # 이름찾기
            cnt = 0 # 찾은 학생의 위치
            for stu in students :
                if stu[1] == search :                   
                    break
                cnt += 1   
            if cnt == len(students) :
                print('{} 학생이 없습니다'.format(search))
            else:
                choice = input('{} 학생을 찾았습니다. 삭제하시겠습니까?(1.삭제 2.)'.format(search))
                if choice == '1':
                    print('{}학생의 데이터가 삭제되었습니다'.format(search))
                    del(students[cnt])
                else:
                    print('삭제가 취소되었습니다')
                print(students)
    print('-'*40)
    
    # # 0. 프로그램 종료
    # elif choice == 0:
    #     print('프로그램을 종료합니다.')
    #     break   # 반복문 종료