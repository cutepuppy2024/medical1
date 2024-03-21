# 숫자를 1개를 입력받아 출력하시오.   # 리스트를 사용했을 때의 문제는 : 복사할 때 !!
# 1. 숫자 1개 입력
# 2. 숫자 1개 출력

num = input('숫자를 입력하세요')  # str
print(num)

# 숫자 2개
num = int(input('숫자를 입력하세요 >>'))
num2 = int(input('숫자를 입력하세요 >>'))
print(num)
print(num2)

# 숫자의 합을 입력하라
print(num + num2)

# 숫자 5개를 입력받아 5개 출력하시오    # 저장할지, 어디에 저장할지, 어떻게 빼올지
nums = []
for i in range(0,5):
    nums.append(int(input('숫자를 입력하세요>>>')))
print(nums)

numA = [0]*5
for i in range(0,5):
    numA[i] = int(input('숫자를 입력하세요'))
print(numA)

numB = [0]*5
for i in range(len(numB)):
    print(numB)

nums1 = [i for i in range(5)]
print(nums1)

numC = []
i = 0
while i <= 5:
    n = int(input('숫자를 입력하세요 >'))
    numC.append(n)
    i += 1
print(numC)


numD = [1,2,3,4,5]
# 5개의 합을 구해보세요
sum = 0
for num in numD:
    sum += num
print('합계 :',sum)

j = 0
sum1 = 0
for j in range(len(numD)):
    sum1 += j
    print('합계 :',sum1)
    