# 반복문 for문 while문
'''
for i in range(시작,끝+1,증감값)
    수행할문장
    
while 조건식   #참일 경우에만
    실행할문장

변수 = 시작값  # ex) i = 0 (변수선언)
while 변수 < 끝값 : # 이 조건이 참일때
    반복구문
    변수 = 변수 + 증가값  # i = i +1
'''

# for 문으로 안녕하세요 를 3번 출력
for i in range(3):
    print('for : 안녕하세요')
   
# while문으로 작성 
i = 0
while i < 3 :
    print('while : 안녕하세요')
    i = i + 1
    
# for 문으로  0-10까지 출력
# while 문으로 0-10까지 출력

for i in range(11):
    print(i,end=' ')
print()

i = 0
while i < 11 :
    print(i,end=' ')
    i += 1   
print() 
    
# while 을 사용해서
# 해보세요
# 1 - 10 사이의 3의 배수를 출력해보세요 : 3,6,9
i = 1
while i < 11 :
    print(i,end=' ')
    i += 3
print()

j = 1
while j < 11 :  # 등호, 부등호는 알아서 맞게 사용하면 됨
    if j% 3 == 0 :    # 출력을 위한 조건
        print(j, end=' ')
    j += 1            # 조건만족

# 1-100 사이의 홀수를 출력
for i in range(1,101):
    if i%2 == 1 :
        print(i,end=' ')
print() 

n = 1
while n <= 100 :
    if n%2 == 1 :
        print(n,end=' \t')
    n += 1
print()




# 1-100까지의 합을 구해보세요
p = 0
sum = 0
for p in range(1,101) :
    p += 1
    sum += p
print(sum)
print()   
    
q = 0
sumA = 0
while q <= 100 :
    q += 1
    sumA += q-1  # 맨 처음에 1이 더해진 값이 될것이므로
print(sumA)
print()


# while True : # 무한히 반복시키고자 할 때 사용  # 무한루프가 되면 => 아래의 명령어가 흐리게 나온다. 그래서 제거해 주어야 함
#     print('ㅋ', end ='')
# while 조건문이 참인경우 반복
# 때문에 while True는 무조건 참이기 때문에 무한히 반복됨
# 무한루프에 들어가면 control + c를 눌러서 강제종료할 수 있다

# while 문을 사용할 때 조건문을 잘 만드는게 중요하다.
# while 1 ==1 :
#     print('ㅋ',end ='')

# break, continue
# break 반복문을 빠져나와서 다음단계를 수행한다.
# n =0
# while n <100:
#     print(n, end =' ') # n = 0 n =1
#     if n == 4:
#         break
#     n = n + 1
#     print('-----------')
    
    
breakletter = input('중단할 문자를 입력하세요 >>')
for letter in 'python':
    if letter == breakletter:
        break
    print(letter)
    
while True:   # 위의 과정들이 무조건 참이니 계속 반복하라는 의미
    n = input('숫자를 입력해주세요(종료: 0)')
    if n == '0' :
        print('종료되었습니다')
        break