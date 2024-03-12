

money = input("교환할 돈의 값을 입력하세요 >>")
money = int(money)

M50000 = money//50000
M10000 = (money%50000)//10000
M5000 = ((money%50000)%10000)//5000
M1000 = (((money%50000)%10000)%5000)//1000

print('입력한 금액: {}'.format(money))
print('50000원권 : {}'.format(M50000))
print('10000원권 : {}'.format(M10000))
print('5000원권: {}'.format(M5000))
print('1000원권: {}'.format(M1000))

# 순차적 적용(update시키는 방법으로)

money = input("교환할 돈의 값을 입력흐세요 >>")
money = int(money)

c500 = 0
c100 = 0
c50 = 0
c10 = 0

money = input("교환할 돈의 값을 입력하세요 >>")
money = int(money)
c500 = money//500 # 몫
print('500원권: {}'.format(c500))
money %= 500
print(money)
c100 = money//100 # 몫
print('100원권 : {}'.format(c100))
money %= 100 
print(money)
c50 = money//50
print('50원권 : {}'.format(c50))
money %= 50
print(money)
c10 = money//10
print('10원권:{}'.format(c10))
money %= 10
print('잔돈: {}'.format(money))