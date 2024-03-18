# 다른 파일에 있는 함수를 끌어와서 쓸 때
# from Module1 import func1

# 모듈의 종류
# 1) 사용자 정의 ex) lotto
# 2) 표준 : 파이썬 제공 ex) math
# 3) 서드파티 : 파이썬 아닌 외부회사나 단체에서 제공

# 1
import lotto
# 2
from lotto import num_generate # (함수명)
# 3
from lotto import  *
# 4
import lotto as lo   # 모듈명을 줄여서 사용가능. 별칭부여


l = [0]*45

# 1
lotto.screen()

# 2 
num_generate(l)

# 3
screen(l)   

# 4
lo.screen(l)
lo.num_generate(l)

#------------------------------------------------------------

import math
from math import*                           
import math as m  # 모듈명을 줄여서 사용가능. 별칭부여


print(math.sin(1))
print(math.cos(1))
print(math.tan(1))


print(math.floor(12.2))

print(m.ceil(12.2))

print(dir(m))




# clear




