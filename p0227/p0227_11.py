num = []
# for 문을 사용해서 1-10까지 숫자를 num채우세요
for i in range(1,11):
    num.append(i)
print(num) #[1,2,3,4,5,6,7,8,9,10]

n1 = 10
for i in range(1,n1+1):
    num.append(i)
print(num)

# 한 줄로도 표현할 수 있다
num1 = [i for i in range(1,11)]  # good!!

num2 = []
# 1-10까지의 짝수를 num2에 넣으세요
for i in range(1,11):
    if i%2 == 0:
        print(i)
        num2.append(i)
print(num2)

for i in range(1, n1+1):
    if i%2 == 0:
        print(i)
        num2.append(i)
print(num2)

# 1~ 10까지의 합 for 문을 사용해서 구할 수 있음

    
# num 리스트를 사용해서 1-10까지의 합을 구해보세요
# num 리스트 내의 숫자들의 합을 구하세요
num = [1,2,3,4,5,6,7,8,9,10]
sumA = 0
for i in num:
    print(i, end ='')
    sumA += i
print(sumA)

sumB = 0
for i in range(len(num)):
    print(num[i],end='')
    sumB += i
print(sumB)


s3 = 0
for n in num2:
    s3 = s3 +n
print(s3)   

s4 = 0   
for i in range(len(num2)):
    s4 = s4 + num2[i]
print(s3,s4)


for i in range(num[0],num[-1]+1):
    sumA += i
print(sumA)

# num2리스트 내 숫자들의 합을 구하세요