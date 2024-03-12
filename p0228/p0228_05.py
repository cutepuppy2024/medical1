# 1. 1-10 의 합
s1 = 0
for i in range(1,11):
    s1 += i
    print(s1)
print('1-10의 합은 {} 입니다'.format(s1))

# num 리스트 안에 있는 값들의 합
num = [1,2,3,4,5,6,7,8,9,10]
s2 = 0
for i in num:
    s2 += i
    print(s2)
print('num리스트 안에 있는 값들의 합은 {} 입니다'.format(s2))

# num 리스트 안의 짝수들의 합
s3 = 0
for i in range(len(num)):
    if num[i]%2 == 0:
        s3 += num[i]
        print(s3)
print('num리스트 안에 있는 값 중 짝수들의 합은 {} 입니다'.format(s3))