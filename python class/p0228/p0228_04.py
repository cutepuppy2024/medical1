# 1~100까지의 합을 구해보세요

sumA = 0
for i in range(101):
    sumA += i
    print(sumA)
    
s1,s2,s3 = 0,0,0
for i in range(1,101):
    # print(i,end=' ')
    s1 += i
    # print(s1)
    if i%2 == 0:
        s2 =s2 + i
    else: # 홀수
        s3 += i
    
print('1-100까지의 합은 {}입니다'.format(s1)) 
print('1-100까지의 짝수의 합은 {}입니다'.format(s2)) 
print('1-100까지의 홀수의 합은 {}입니다'.format(s3)) 
    
# 짝수의 합
sum2A = 0
for i in range(0,101):
    if i%2 == 0:
        sum2A += i
        print(i,end=' ')
        print('짝수의 합은',sum2A, '입니다')
# 홀수의 합
sum2B = 0 
for i in range(0,101):
    if i%2 != 0:
        sum2B += i
        print(sum2B)