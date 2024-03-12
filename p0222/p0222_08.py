# 반지름을 입력받아
# 원의 둘레와넓이를 출력하시오.(Pi=3.14195, 반지름 =10)
pi = 3.14192
r = input("원의 반지름의 값을 입력하시오 >>")
r = int(r)
result = 2*pi*r
result = pi*r**
print('{}*{}*{}={}'.format(2,pi,r,result))
print('{}*{}**={}'.format(pi*r**2))


# 풀이
r = input("원의 반지름의 값을 입력하시오 >>")
r = int(r)
pi = 3.14195

print('원의 넓이 : {}', format(pi * (r**2)))
print('원의 둘레 :{}'.format(2*pi*r))