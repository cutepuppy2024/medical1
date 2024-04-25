import time


# 타임슬립 ; 일정시간동안 멈추게 하는 함수      
for i in range(100):
    if i%10 == 0:
        time.sleep(3)   
        pass
    print(i)
    
    
    
# 랜덤타임슬립    
import random

for i in range(1,100+1):
    if i%10 == 0:
        num = random.randint(1,5)
        print(num,'초 대기')
        time.sleep(num)
        pass
    print(i)
    
    
    
# clear