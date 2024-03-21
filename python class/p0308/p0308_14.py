# 문자 정렬 center(), ljust(), rjust(), zfill()

ss = '파이썬'

print("1234567890")
print(ss.ljust(10))
print(ss.center(10,'*'))   # 가운데 정렬, 빈 공백을 *로 채워줌   ***파이썬****
print(ss.rjust(10))    
print(ss.zfill(10))    # 빈공간들을 0 으로 채워줌 0000000파이썬

