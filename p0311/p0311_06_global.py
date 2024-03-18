sum = 0

def plus(num):
    global sum
    sum += sum + num
    
n_input = int(input('숫자를 입력하세요 >> '))
plus(n_input)   # 매개변수가 틀리면 error

print('총합 :',sum)