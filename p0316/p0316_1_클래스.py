# <  클래스  >
# 클래스 : 사용자 정의 변수 = 함수도 포함
#       => 목적 : 변수선언을 한 번에 하기 위해

# class Car:       # 클래스의 형태 : 항상 첫글자는 대문자 사용
#     color = "white"
#     door = 5
#     length = 4710
#     width = 1800
#     displace = 1600

# def func():      # 함수의 형태
#     pass


# c1 = Car()       # 클래스 객체선언 : Car 클래스에 있는 모든 변수를 사용함
# print(c1.length) # 호출만 하면 됨
# c2 = Car()
# c3 = Car()


# a_l1 = 4710
# (print(a_l1))
# a_w1 = 1800
# a_d1 = 1600

# a_l2 = 4710
# a_w2  = 1800
# a_d2 = 1600

# a_l3 =4710
# a_w3 = 1800
# a_d3 = 1600

# # 컴퓨터에서는 이것을 하나의 묶음으로 인식하지 않는다

# ================================================================================

class Car:  # 클래스 선언
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0
    
    def upSpeed(self,sp):
        self.speed += sp
    
    def downSpeed(self,sp):
        self.speed -= sp

# 객체선언을 할 때마다 제품(Car)이 한개씩 생산        
c1 = Car()  # 객체선언
print('색상 :',c1.color)
c1.color = 'red'
print('변경된 색상 :',c1.color)

c2 = Car()
print('색상 :',c2.color)