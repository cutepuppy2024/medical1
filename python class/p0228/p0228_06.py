



a = 10
b = 8
a,b = b, a     # a가 b보다 큰 경우 오류가 나는데 이렇게 정의내려주면 오류나지 않는다
print('a',a)
print('b',b)


# 두 수를 입력받아 n1 부터 n2 까지의 합을 n1, n2 비교해서

n1 = int(input('첫번째 숫자를 입력해 주세요 >>>'))
n2 = int(input('두번째 숫자를 입력해 부세요 >>>'))
sum = 0

if n1> n2:
    n1,n2 =n2,n1

for i in range(n1,n2+1) :
    sum += i
    print(sum)
print('{}부터 {}까지의 합은 {}입니다.'.format(n1,n2,sum))

n1 = int(input('첫번째 숫자를 입력해 주세요 >>>'))
n2 = int(input('두번째 숫자를 입력해 부세요 >>>'))   
odd_list = []
for i in range(n1,n2+1) :     # 숫자 한번씩만 입력해서 바로  odd_list나오게 하려면?  
    if i%2 == 1:
        odd_list.append(i)
        print(odd_list)
print('{}부터 {}까지의 숫자들 중 홀수는 {}입니다'.format(n1,n2,odd_list))




