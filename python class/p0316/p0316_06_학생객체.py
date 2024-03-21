class Student: # 클래스선언 = 설계동
    # stuNo = 0          # init의 경우 생략가능, 미리 정의를 내려 주는 것도 좋다
    # stu_name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    
    def __init__(self,stuNo=0,stu_name="",kor =0, eng = 0, math = 0):
        self.stuNo = stuNo
        self.stu_name = "name"
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        self.rank = 0
        

# 1,홍길동,99,99,87,285,95.0,1
# 2,유관순,98,93,87,278,92.67,3
# 3,이순신,88,76,30,194,64.67,6


# 기본생성자
s1 = Student()
s1.stuNo = 1
s1.stu_name = "홍길동"
s1.kor = 99
s1.eng = 99
s1.math = 87
s1.total = s1.kor + s1.eng + s1.math
s1.avg = float('{:.2f}'.format(s1.total/3))
s1.rank = 1
print(f'홍길동 : {s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng}{s1.math},{s1.total},{s1.avg},{s1.rank}')


# 전체생성자
s2 = Student(2,'유관순',98,93,87)
print(f'유관순 : {s2.stuNo},{s2.stu_name},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}')
s3 = Student(3,'이순신',88,76,30)
print(f'이순신 : {s3.stuNo},{s3.stu_name},{s3.kor},{s3.eng},{s3.math},{s3.total},{s3.avg},{s3.rank}')


stu_list = [s1,s2,s3]
print(stu_list)   # 리스트의 형태로 출력되지 않는다