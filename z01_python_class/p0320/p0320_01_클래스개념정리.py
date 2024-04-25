class Car:
    count = 0                              # 클래스변수 인식
    
    def __init__(self,color='black',speed=0):   # 키워드변수 : 매개변수의 default값
        self.color = color                 # init 안에 변수선언 - 인스턴스변수
        self.speed = speed
        # 클래스 변수선언
        # Car.count = 0
        
        
# class 사용하기 위해서는 인스턴스 선언
c1 = Car()                                 # 인스턴스(객체)선언
c1.color = "white"
print("c1.color :",c1.color)  
print("c1.speed :",c1.speed)   
Car.count = 10                             # 클래스변수에 값을 ins
print("c1.count :",c1.count)   


c2 = Car()
c2.color = "red"
print("c2.color : ", c2.color)
print("c2.color : ", c1.color)                            # 클래스에서의 값: 변경되지 않음을 비교해보기
print("c2.count : ", c2.count)             # c1 class에서 Car.count를 클래스변수로 선언했기 때문에 모두가 변경
Car.count = 200
print("c1.count :", c1.count)
print("c2.count :", c2.count)
c2.door = 4                                # 변수가 선언이 되면서 클래스 안에 들어간다
print("c2.door :", c2.door)
c2.count = 1                               # 기존 클래스변수를 지우고 인스턴스변수를 다시 생성, 규정한 값만 바뀜 => 에러, 혼선의 가능성
print(c2.count)
print(c1.count)
c3 = Car()
print(c3.count)



c2.count = 100                   # (X)     # 클래스변수로 사용하기 원한다면 인스턴스변수의 형태로 쓰면 안된다
print("c1.count :",c1.count)
print("c2.count :",c2.count)

Car.count = 100
print("c1.count :",Car.count)  # (O)
print("c2.count :",Car.count)

# ----------------------------------------------
Car.count = 10                             # 클래스변수 변경
print("c1.count :",Car.count)     
print("c2.count :",Car.count)


