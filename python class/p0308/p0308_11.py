# <  strip, replace  >

# strip 공백제거 => 문자 사이에는 적용되지 않는다
s1 = '    파이썬     '
s2 = '파이썬'

print(s1.strip())    
print(s1.lstrip())   # lstrip -left 공백제거 / rstrip - right 공백제거
print(s1.rstrip())

if s1.strip() == s2:
    print('맞습니다')
else:
    print('틀립니다')
    
if s1.lstrip() == s2:
    print('맞습니다')
else:
    print('틀립니다')
    
if s1.rstrip() == s2:
    print('맞습니다')
else:
    print('틀립니다')
    
   
s_input = input('지금 현재 배우는 과목은? >>').strip()   # 입력시 공백제거 위해 사용
if s_input == s2 :
    print('정답입니다')    
else:
    print('오답입니다.')
    
# replace  :  문자열을 다른 문자열로 대체
ss = 'apple은 당도가 높고, apple의 색상은 빨강, 녹색이 있습니다'  # ctrl + f : replace 사용할 수 있음
print(s1.replace('파','자'))
print(s1.replace('apple','사과'))
print(s1.replace(' ',''))  


news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다.\
2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. \
    지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 \
        사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
print(news.replace(" ",''))  # => 문자 사이의 공백을 지우기 위해서는 replace
#그룹 => group으로 변경 
print(news.replace('그룹','group'))

