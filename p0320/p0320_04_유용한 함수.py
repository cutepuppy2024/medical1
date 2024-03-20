class Student:
    def __init__(self,name,total):
        self.name= name
        self.total = total
    def __str__(self):
        return f"이름 : {self.name}, 총점 : {self.total}"
    
    def __del__(self):
        return "클래스가 소멸될 때 실행"           
    
    def __add__(self,s):
        return self.total+s.total
    
    def __gt__(self,s):  # 크거나 같다라고 비교할 때
        return self.total>s.total
        # print("> 클래스간 비교를 하면 이 함수가 호출이 됨.")
    
    def __eq__(self,s):
        return self.name == s.name and self.total == s.total
            
        
    
        
        
s1 = Student("홍길동",100)
s2 = Student("유관순",90)
s3 = Student("이순신",95)
s4 = Student("홍길동",100)

#------------------------------------------------
print(s1)               # 클래스를 출력할 때 : str 함수 

print(s1+s2)            # 클래스를 더하기 할 때 : add 함수

print(s1>s2)            # 클래스는 비교가 불가능 : 비교대상, 기준에 대한 정의필요 => __gt__ 메소드를 생성하면 호출
print(s2>s3)

print(s1)                         
print(s4)
print("s1==s4:", s1==s4)           # False -> 비교가 불가능하므로: 객체 주소가 비교되는 것임
print("s1==s2:", s1==s2)

# a_list =[10,20,30,40]
# b_list =[2,3,4,5]
# print(a_list>b_list)

