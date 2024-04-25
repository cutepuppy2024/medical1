# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo에는 carCount 숫자를 이용해서 carNo를 넣으시오 
# color= "white", door=5, tire=4, speed,
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 -10씩 감소


# c1 - white, 5,4,0 -> speed 30이 되도록
# c2 - red, 5,4,0 -> speed 100이 되도록
# c3 - silver,5,4,0 -> speed 70이 되도록
# car_list 추가하고

# car_list에 있는 모든 객체의 모든 color, door, tire, speed  모두 출력하시오

class Car:
    carCount = 0
    carNo = 0
    
    def __init__(self,color='',door=5, tire=4, speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1
        self.carNo = Car.carCount
        
    def up_speed(self,speed):
        speed += 10
        
    def down_speed(self,speed):
        speed -+ 10
 
 
        
car_list = []

c1 = Car("white",5,4,0)
for i in range(3):
    c1.up_speed(i)   
car_list.append(c1) 
print(c1.color,c1.door,c1.tire,c1.speed)

c2 = Car("red",5,4,0)
for i in range(10):
    c2.up_speed(i)
car_list.append(c2)
print(c2.color,c2.door, c2.tire, c2.speed)

c3 = Car("silver",5,4,0)
for i in range(7):
    c3.up_speed = 70
car_list.append(c3)
print(c3.color, c3.door, c3.tire, c3.speed)


for i in range(len(car_list)):
    print(car_list[i].color, car_list[i].door, car_list[i].tire, car_list[i].speed)
    
    
    



    



 
        
    
 


