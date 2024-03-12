# 변수
# 기본: bool, int, float, string
# list, tuple, dict
a = True
b = False
print('bool형은 {},{}가 있다'.format(a,b))

c = 45
print('int형은 정수 {:d} 와 같은 숫자'.format(c))
print('%d'%(c))

d = 3.123568
print('float 형은 실수 {:.2f}와 같이 소숫점이 있는 숫자'.format(d))

e = '문자' # string type
print('문자열입니다')
print(e+'입니다')
print(e,'입니다')
print('{:s}입니다'.format(e))

# input() -  콘솔창에서 입력을 받는다
print('글자를 콘솔창에 보여준다')# 
str1 = input('입력하세요 >> ')
print('{}은 입력한 변수값입니다.'.format(str1))

n1 = input('첫번째 숫자를 입력하세요 >>')
n2 = int(input('두번째 숫자를 입력하세요 >>'))
# n1 * n2 값을 출력해보세요
# 숫자로 출력 #30
print(n1*n2)
# input()을 통해서 입력받는 것은 문자다
# 10이라고 입력해도 컴퓨터는 '10'으로 인식
# int를 입력하지 않으면 숫자를 문자로 인식하기 때문
print(int(n1)*n2)



