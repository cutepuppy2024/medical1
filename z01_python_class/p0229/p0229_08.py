# 1 - 100까지 더하는데,
# 총 합이 100이 넘었을 때 수를 출력하세요
# 1 + 2 + .... 

# 1 -10 까지 더하는데 총합이 4가 넘는 순간의 수를 출력
# 1 + 2+ 3  => 3 출력

sum = 0
i = 0
while sum <= 100:
    i += 1
    sum += i
    if sum < 100:
        continue
    else:
        print('종료')
print(i,sum)
print('{}까지 더하여 100을 처음 넘기는 숫자는 {}입니다'.format(i,sum))

sumA = 0
j = 0
while True:
    j += 1
    sumA += j
    if sumA < 100:
        print('{}까지 더한 경우 나오는 숫자는 {}입니다.'.format(j,sumA))
    else:
        print('{}까지 더하여 나온 숫자는 {}입니다.'.format(j,sumA))
        break 
 
p = 0   
sumB = 0
for p in range(1,101):
    sumB = sumB + p
    if sumB > 100:
        break
print('수:', p)
print('총합 :', sumB)
    
# while
total = 0
q = 1
while i <= 100 :
    total += q
    if total > 100:
        break
    q +=1
print('수:',q)
print('총합 :', total)
# for while 둘중 하나를 사용해서


