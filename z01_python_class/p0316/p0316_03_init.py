class Car:                  # 기본값을 입력, 출력시 다른 부분만 변경하여 출력
    car_name = "드뉴아반떼"
    color = "white"
    door = 5
    length = 2000
    width = 1000
    speed = 0
    
    def up_speed(self,s): # 클래스 내에는 무조건 self를 넣어주어야 한다
        self.speed += s
    

# 1. 기본 생성자를 사용한 객체선언                                       
# 철수의 차 생산
c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60)              # 현재 speed 60을 더해 줌
c1.up_speed(40)              # 현재 속도는 얼마?  100
c1.up_speed(50)              # 현재 속도는 얼마?  150
c1.speed = 50                # 현재 속도는 얼마?  50   

# 영희의 차를 1대 생산해서, 색상은 greed, speed, 나머지 동일, speed = 100
c2 = Car()
c2.car_name = "드뉴아반떼"
c2.color = "white"
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.speed = 0
c2.up_speed(100)


# 반장차 - 디올뉴그랜저, 화이트펄, 길이: 2500, 폭: 1400, speed = 150
c3 = Car()
c3.car_name = '디올뉴그랜저'
c3.color = 'white pearl'
c3.door = 5
c3.length = 2500 
c3.width = 1400
c3.up_speed = 1500


print("철수차 성능 :",c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)
print("영희차 성능 :",c2.car_name, c2.color, c2.door, c2.length, c2.width, c2.speed)
print("반장차 성능 :",c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)


# ==============================================================================================================

class Car:              
    # 생성자
    # def __init__(self,car_name="",color="",door,length,width,speed):    # 매개변수로 클래스 내에 선언된 변수와 다른 값이다
    def __init__(self,car_name="",color="",door=5,length=2000,width=1000,speed=0):    # 키워드 매개변수
                                                                  # def __init__(self,c_n,c,d,l,w,s):    # 매개변수로 클래스 내에 선언된 변수와 다른 값이다
            self.car_name = car_name                              # 클래스 내의 변수를 찾는다
            self.color = color    
            self.door = door    
            self.length = length
            self.width = width
            self.speed = speed  
    def up_speed(self,s):
        self.speed += s
            
# 2. 생성자를 사용한 객체 = 인스턴스 선언
c4 = Car()
c4.car_name = "드뉴아반떼"
c4.color = "white"
c4.door = 5
c4.length = 2000
c4.width = 1000
c4.speed = 0

print("차 성능 :",c4.car_name, c4.color, c4.door, c4.length, c4.width, c4.speed)


c1 = Car("드뉴아반떼", "white", 5,200,1000,60)
print("철수차 성능 :",c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)

c2 = Car("드뉴아반떼","green",5,200,1000,100)
print("영희차 성능 :",c2.car_name, c2.color, c2.door, c2.length, c2.width, c2.speed)

c3 = Car("디올뉴그랜저","화이트펄",5,2500,1400,1500)
print("반장차 성능 :",c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)




# clear