# student 클래스 생성, 파일 불러와서 클래스에 저장후 출력하시오

class Student:
    count = 1
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        
        if stuNo == 0 :
            self.stuNo = Student.count  # stuNo가 0이면 클래스변수 사용
        else:
            self.stuNo = stuNo   # 그렇지 않으면
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = '{:.2f}'.format(self.total/3)     
        self.rank = rank

           
    def __str__(self):
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'
            

# 파일불러와서 클래스로저장
students = []
f = open("stu.txt",'r',encoding='utf8')
while True:
    t = f.readline()
    if t == '': break
    s_list = t.split(",")    # 리스트지정
    a = Student(s_list[1], int(s_list[2]), int(s_list[3]),int(s_list[4]), int(s_list[0]),int(s_list[7]))  #  클래스 객체선언
    students.append(a) # 리스트에 클래스 저장

f.close() 

Student.count = len(students)+1 


# ------------------------------------------
# 메인 프로그램 시작
# ------------------------------------------

cnt= 1 
search_txt= [
        '',"찾고자 하는 학생 이름을 입력하세요.>> ",
        "몇 점이상 검색하시겠습니까?>>",
        "몇 점이하 검색하시겠습니까?>>"
    ]

     
while True:
    print('-'*40)
    print('\t[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생성적검색')
    print('0. 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요.>>')
    choice = int(choice)
   
    if choice == 1: 
        while True :
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if name=="0":
                print("학생 입력을 취소합니다.")
                break
            kor = int(input("국어점수를 입력하세요."))
            eng = int(input("영어점수를 입력하세요."))
            math = int(input("수학점수를 입력하세요."))
            s = Student(name,kor,eng,math)   # 객체선언
            students.append(s)               
            print("입력 데이터 :",s) #list -> dict    

    elif choice == 2: 
        print('\t[ 학생성적출력 ]')
        print('-'*65)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print('-'*65)
        for i in students:  
            print(i)       # students리스트의 i번째 클래스 => 객체 호출시 __str__로 print
        print()

    elif choice == 3:  # 학생검색
        while True:
            print("\t[ 학생성적 검색 ]")
            print("-"*40)
            print("1. 학생이름으로 검색")
            print("2. 점수이상 검색")
            print("3. 점수이하 검색")
            print("0. 이전화면 이동")
            choice = int(input("원하는 번호를 입력하세요.>> "))
            if choice == 0:
                print("이전화면으로 이동합니다.")
                break
            # 학생검색 프로그램 부분
            if choice == 1:
                search = input(search_txt[choice])
            else:
                search = int(input(search_txt[choice]))
                # 전체리스트에서 학생검색
            s_list = []
            for i in students:
                if choice == 1:
                    if i.name.find(search) != -1:
                        s_list.append(i)
                elif choice == 2:
                    if i.total >= search:
                        s_list.append(i)
                elif choice == 3:
                    if i.total <= search:
                        s_list.append(i)        
            if len(s_list) != 0:
                print('\t[ 학생성적출력 ]')
                print('-'*65)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
                print('-'*65) 
                for i in s_list:
                    print(i)
            else:
                print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ")   

                
    elif choice == 4:
        # 학생이름으로 검색
        # 1. 이름으로 학생을 검색
        # 2-1. 찾았으면 과목 선택
        # 2-1-1. 과목리스트 출력
        # 2-1-2. 국어선택
        # 2-1-3. 국어점수 출력 후 국어점수 입력
        # 2-1-4. 국어점수 변경 후 이전화면 이동
        
        # 2-2. 못 찾았으면 다시 이전화면으로 나옴    
    
        search = input('검색')
        chk = 0
        if search == '0':
            break
        for stu in students:
            if stu.name == search:
                break
            chk += 1
        
        if chk == len(students):
            print('찾고자 하는 학생이 없습니다. 다시 검색하세요')
            
        print("찾고자 하는 학생의 위치 :", chk)
        print(students[chk])
        
        s_input = int(input("수정하려는 과목을 선택하세요.(0.취소)>>"))
        

        
        
# ------------------------------------------------------
# 함수부분
#--------------------------------------------------------


# def stu_main_print():

# def stu_insert():

# def stu_print():
    
# def search_title_print():
    
# def stu_search(choice):
        
# def stu_search(choice):
         