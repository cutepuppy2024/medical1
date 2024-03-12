students = []
cnt = 0

while True:
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력') # 이름, 국, 영, 수 점수를 입력을 받으면 [번호, 이름, 국,영,수,총합,평균]
    print('2. 학생성적수정') # 국, 영, 수 점수를 수정해 볼 수 있음. (유의: 국어를 바꾸면, 합, 평균)
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')  ###### 전체출력 !!!!
    print('5. 힉생검색출력')
    print('6. 등수처리')
    print('0. 프로그램종료')
    print('-'*35)
    choice = input('원하는 번호를 입력하세요. >>')
    print('입력하신 번호는 {}입니다'.format(choice))
    choice = int(choice)
    if choice == 1:
        print('학생성적입력입니다')
        name = input('학생이름을 입력하세요 >>')
        kor = int(input('국어성적을 입력하세요 >>'))
        eng = int(input('영어성적을 입력하세요 >>'))
        math = int(input('수학성적을 입력하세요 >>'))
        total = kor + eng + math
        avg = (kor + eng + math)/3
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1,name,kor,eng,math,total,avg))
        stu1 = [1,name,kor,eng,math,total,avg]
        students.append(stu1)
        print(students)
    elif choice == 4 :
        print('학생출력을 선택하셨습니다')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
        for i, p_stu in enumerate(students):
            print('{}'.format(students[i][1]))
            print('{}'.format(p_stu[1]))
            # print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(students[i][0],))
            # print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(p_stu[0],))
    elif choice == 5:
        print('학생검색을 출력하셨습니다')
        for p, s_stu in enumerate(students):
            search_Name = input('검색할 학생의 이름을 입력하세요 >>')
            if search_Name in p:
                print(search_Name,'이 존재합니다')
                print(p)
            else:
                print('존재하지않습니다')
    elif choice == 3:
        print('학생검색삭제를 출력하셨습니다')
        for d, s_del in enumerate(students):
            del_Name = input('검색하여 삭제하실 학생의 이름을 입력하세요 >>')
            if del_Name in d:
                print(del_Name,'이 존재합니다')
                del(students[d])
                print(students)
            else:
                print('검색하신 학생의 이름이 존재하지 않습니다')
            
        
        
        
        
        
        
        
        
        # print('학생성적수정을 입력하셨습니다')
        # #국,영, 수 중에 선택 =>
        # print('수정하실 성적을 번호로 입력하세요 1.국어 2.영어 3.수학')
        # cor_sub = int(input('수정하실 과목번호를 입력해 주세요 >>'))
        # if cor
        # print('{}를 선택하셨습니다'.format(cor_sub))