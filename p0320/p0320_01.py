class Car:
    count = 0                              # 클래스변수 인식
    
    def __init__(self,color='black',speed=0):   # 키워드변수 : 매개변수의 default값
        self.color = color                 # init 안에 변수선언 - 인스턴스변수
        self.speed = speed
        
        
# class 사용하기 위해서는 인스턴스 선언
c1 = Car()                                 # 인스턴스(객체)선언
c1.color = "white"
print("c1.color :",c1.color)     
Car.count = 10                             # 클래스변수에 값을 ins
print("c1.count :",c1.count)   
print("c1.speed :",c1.speed)

c2 = Car()
c2.color = "red"
print(c2.color)
print(c1.color)                            # 클래스에서의 값: 변경되지 않음을 비교해보기

c2.count = 100                      # (X)  # 클래스변수로 사용하기 원한다면 인스턴스변수의 형태로 쓰면 안된다
print("c1.count :",c1.count)
print("c2.count :",c2.count)

Car.count = 100
print("c1.count :",Car.count)       # (O)
print("c2.count :",Car.count)