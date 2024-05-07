# 반복문

# for 변수 in range(시작값, 끝값 +1, 증가값) :

for i in range(3): # i = 0,1,2
    print('안녕')
    # i = 0일때
    # i = 1일때
    # i = 2일때
    
for i in range(3):  # i = 0,1,2
    print(i)
    
# i = 0,1,2,3...
# i = 1,2,3,4,5....
for i in range(100):
    print(i+1)
    
sum1 = 0
for i in range(1,6,1):
    sum1 = sum1 + i
    
# 숫자 한개를 입력받아서 1부터 입력한 수까지의 합을 구하세요
num = int(input('숫자를 입력하세요 >>'))
sum = 0
for i in range(1,num+1):
    sum += i
print(sum)

n1 = 100  # 1에서 100까지 (1 +... + 100)
sum100 = 0
for i in range(1,n1+1):
    # print(i, end='')
    sum100 += i
print(sum100)

# for i in range(1,) :
#     합계
# 합계 출력

# 짝수의 합만 구함 (2+4+6+8+..+100)
sum2N = 0
for i in range(0,101,2):
    sum2N += i
print(sum2N)

sum = []
sumA = 0
for i in range(101):
    pass
    if i%2 == 0:
        print(i, end=(''))
        sumA += i
        sum.append(i)
        print(sum)
        print(sumA)
sumA = 0       
for i in range(n1+1):
    pass
    if i%2 == 0:
        print(i, end=(''))
        sumA += i
print("{}부터 {} 까지의 짝수의 합은 {}입니다.".format(1,n1,sumA))

# 1-10까지의 곱
multiple = 1
for i in range(1,11):
    multiple *= i
print(multiple)
