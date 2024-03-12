#continue :
# 반복문에서 남은 문장을 수행하지 않고 다음단계로 넘어감

n = 0
while n < 100:
    n += 1
    if n%2 == 0:  # 짝수일때
        # break
        continue  # 아래에 어떤 수가 있든 건너뛰고 위로 올라가서 반복수행 
    print(n, end = ' ')
print()
    
breakletter = input('중단할 문자를 입력하세요 >>')
for letter in 'python':
    if letter == breakletter:
        continue                        # 해당문자만 건너뛰고 다시 반복, break는 즉시 중단되어 이후과정은 출력되지 않음
    print(letter)
    
    
# break는 문자를 만나면 프로그램이 종료되는데 (반복문이 종료)
# continue같은 경우는 문자를 건너띄고 출력이 됨.

#pass : 문법적으로 필요는 하지만 어떤 동작도 원하지 않을 경우 사용
# 즉, 어떤 것도 수행하지 않고 해당부분을 패스
breakletter = input('중단할 문자를 입력하세요 >>')
for letter in 'python':
    if letter == breakletter:
        pass                        # 별로 사용하지 않는다
    print(letter)