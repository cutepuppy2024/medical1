# 다른 파일에 있는 함수를 끌어와서 쓸 때
# from Module1 import func1

# 모듈의 종류
# 1) 사용자 정의 ex) lotto
# 2) 표준 : 파이썬 제공 ex) math
# 3) 서드파티 : 파이썬 아닌 외부회사나 단체에서 제공

import lotto
from lotto import num_generate
from lotto import  *
import lotto as lo   # 모듈명을 줄여서 사용가능. 별칭부여

l = [0]*45
# while True:
    # lotto.screen()

screen(l)   
num_generate(l)

lo.screen(l)
lo.num_generate(l)


# import math
# from math.(floor,sin,cos,tan,ceil)// from 이름.함수명()
import math as m  # 모듈명을 줄여서 사용가능. 별칭부여



print(m.ceil(12.2))

print(dir(m))




# clear




