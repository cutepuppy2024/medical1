# 1~5 까지의 합계를 구하세요
sum = 1+2+3+4+5
print(sum)
total = 0  # t = 0
total = total +1 # t = 1
total = total +2 # t = 1+2
total = total +3 # t = 1+2+3
total = total +4 # t = 1+2+3+4
total = total +5 # t = 1+2+3+4+5

t = 0
for i in range(1,6,1): # i = 1,2,3,4,5
    t += i
print(t)

# 1에서 10까지의 합을 구해보세요 for
# 1에서 100까지의 합을 구해보세요

sum10 = 0
for i in range(1,11):
    sum10 = sum10 +i
    print(i)
print('1부터 10까지의 합은 : {}입니다'.format(sum10))

sum100 = 0
for i in range(1,101):
    sum100 += i
print('1부터 100까지의 합은: {}입니다.'.format(sum100))

t=0
for i in range(1,11,1):
    t += i
print(t)

t = 0
for i in range(0,10):
    t += i+1
print(t)

t = 0
for i in range(1,101):
    t += i
print(t)


# 입력한 수부터 입력한 수까지의 합을 구해보세요
n1 = int(input('첫번째 숫자를 입력하세요 >>'))
n2 = int(input('두번째 숫자를 입력하세요 >>'))
print(n1,n2)

sumN = 0
for i in range(n1,n2+1):
    sumN += i
print(sumN)



