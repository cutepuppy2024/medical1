class Student:
    count = 1   # 클래스변수 사용 : 저장장소가 단 하나
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank= 0):
        if stuNo == 0:
            self.stuNo = self.stuNo = Student.count
        else: 
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        if rank != 0:
            self.rank = rank
    def __str__(self):   # 객체를 호출하면 출력됨
        return f"학생성적 : {self.stuNo}, {self.name}, {self.kor}, {self.eng}\
            , {self.math}, {self.total}, {self.rank}"
        

   
        
# 파일 불러와서 저장하기
students= []   
f = open("stu.txt",'r',encoding='utf8')
while True:
    s = f.readline()
    if s == '': break
    s_list = s.split(',')
    # 1,홍길동,100,100,99,299,96.67,1
    p = Student(s_list[1],int(s_list[2]),int(s_list[3]),int(s_list[4]),int(s_list[0]),int(s_list[7]))
    students.append(p)

# 리스트 출력
for stu in students:
    print(stu)
    
    









