class Student:
    stuCount = 0  # 클래스 변수
    stuNo = 0  # 인스턴스변수 # 클래스변수선언을 하면 이 수도 클래스변수가 된다
    
    # 생성자: __init__
    # 클래스에 대해 객체선을을 하면 제일먼저 호출되는 함수
    def __init__(self,name='',kor=0,eng=0,math=0,science=0):
        self.name = name
        if kor>100:            # 각 변수 당 제한을 둘 수 있다
            self.kor = 100
        else:
            self.kor = kor
            
        self.kor = kor
        self.eng = eng
        self.math = math
        self.science = science
        self.total = kor + eng + math + science
        self.avg = "{:.2f}".format(self.total/4)
        self.rank = 0
        # Student.stuNo += 1 
        Student.stuCount += 1  # 클래스변수선언 -> 클래스명.변수명
        self.stuNo = Student.stuCount
        
    def stu_print(self):
        print(self.stuNo,self.name, self.kor, self.eng, self.math, self.science\
            , self.total, self.avg, self.rank, sep="\t")
        print("학생성적 : ")
        
    # 객체를 print하면 __str__함수를 제일 먼저 호출함
    
    def __str__(self):
        return f"{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
        
# 매개변수가 있는 개체(인스턴스)선언
s1 = Student("홍길동",100,100,99)   # 객체선언
s2 = Student("유관순",99,99,98)     # 참조변수

print(s1)  # __str__ 함수호출 없으면 주소값 출력





