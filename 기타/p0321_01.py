class Student:
    name = ""
    kor = 0
    
    def __init__(self,name=""):
        pass
    def stu_print(self):
        print("학생성적 출력합니다")
        
class Lotto:
    pass
        
def s_print():
    print("class 밖에 있는 함수")        
            
s = Student()                 # 객체선언할 때 무조건 init() 호출
s2 = Lotto()

print(s)
print(Student())              # 한번만 사용하고자 할 경우

s_print()  

s.stu_print()                 # 클래스  내에 있는 함수는 꼭 객체 선언을 해야 사용가능


if isinstance(s2, Student):   # (객체선언변수, 클래스명)
    print("Student 클래스 변수입니다.")
elif isinstance(s2, Lotto):
    print("Lotto 클래스 변수입니다.")
    
print(type(s2))