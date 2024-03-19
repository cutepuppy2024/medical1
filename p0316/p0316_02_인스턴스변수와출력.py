class Car:                  # 기본값을 입력, 출력시 다른 부분만 변경하여 출력
    car_name = "드뉴아반떼"
    color = "white"
    door = 5
    length = 2000
    width = 1000
    speed = 0
    
    def up_speed(self,s):    # 클래스 내에는 무조건 self를 넣어주어야 한다
        self.speed += s

c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60)              # 현재 speed 60을 더해 줌
c1.up_speed(40)              # 현재 속도는 얼마?  100
c1.up_speed(50)              # 현재 속도는 얼마?  150
c1.speed = 50                # 현재 속도는 얼마?  50   => 직접적으로 값을 쓰는 것은 막는다(보안상, 값 변경을 아무나 할 수 있게 하도록)


speed = 0                  # 클래스도 함수와 동일하게 클래스 외에 선언된 변수값은 내의 값과 다르다
def aaa_speed():
    a_speed += a




# 철수의 차를 1대 생산
c2 = Car()
c2.car_name = "드뉴아반떼"
c2.color = "white"
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.speed = 0
c2.up_speed(100)

color = 'red'    # 변경
speed = 60

print("철수차 성능 :",c1.car_name, c1.color, c1.door, c1.length, c1.width, c1.speed)

# 영희의 차를 1대 생산해서, 색상은 greed, speed, 나머지 동일, speed = 100 설정해서 출력하시오
car_name2 = '드뉴아반떼'
color2 = 'green'
door2 = 5
length2 = 2000
width2 = 1000
speed2 = 100

print("영희차 성능 :",c2.car_name, c2.color, c2.door, c2.length, c2.width, c2.speed)


# 반장차 - 디올뉴그랜저, 화이트펄, 길이: 2500, 폭: 1400, speed = 150
c3 = Car()
c3.car_name = '디올뉴그랜저'
c3.color = 'white pearl'
c3.door = 5
c3.length = 2500 
c3.width = 1400
c3.up_speed = 150

print("반장차 성능 :",c3.car_name, c3.color, c3.door, c3.length, c3.width, c3.speed)

