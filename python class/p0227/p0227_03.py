# list
# 리스트변수명 = [요소1, 요소2, 요소3 ....., 요소n]
# 요소하나하나가 변수(int, bool, float, string, list)
l1 = ['홍길동', 100]
l2 = [[2,4,6],[1,3,5]]
l3 = [True, False, 3.14, 'hello',[1,2], 5]
# l3 = ['true', 'false', 3.14, 'hello',[1,2], 5] # 대문자가 아닌경우 문자로 인식하기 때문에 ''표시를 해 주어야 한다

# 인덱싱: 리스트검색, 접근
# index는 0부터 시작함
print(l1[0]) # 홍길동
print(l2[1][1])# 12에서 3을 출력

# 해보세요 = l3에서
# 13에서 False 출력
# hello출력
# 1 출력
# 5 출력

print(l3[1])
print(l3[3])
print(l3[4][0])
print(l3[-1])

# 인덱싱을 가지고 리스트의 특정 요소의 값을 수정할 수 있다
# l1 = ['홍길동', 100]
l1[1] = 90
print(l1)
l1[0] ='이순신'
print(l1)

# l2 = [[2,4,6],[1,3,5]]
l2[0][2] = 8 # 6>8
l2[1][2] = 7 # 5>7
print(12)

l3 = [True, False, 3.14, 'hello',[1,2], 5]
#해보세요 l3에서
# True -> False
# 3.14 -> 31.4
# 'hello' -> 'hi'
# 2 -> 20 변경해보세요

l3[0] = False
print(l3)
l3[2] = 31.4
print(l3)
l3[3] = 'hi'
print(l3)
l3[-2][1] = 20
print(l3)


# 슬라이싱 : 리스트 자르기
# 리스트명[(시작인덱스):(끝인덱스+1)]
num = [0,1,2,3,4,5,6,7]
print(num[1:6])  # 1이상 6미만을 출력
#[1,2,3,4,5]

str1 = ['a','b','c','d','e','f']
# [c,d] 출력
# [b,c,d,e,f] 출력
# [a,b,c] 출력
# [a,b,c,d,e,f] 출력
# [b,c,d,e] 출력
print(str1[2:4])
print(str1[1:])
print(str1[0:3])
print(str1[0:]) 
print(str1[1:-1])

# 리스트의 길 : len(리스트명)
print(len(l1))
print(len(l2))
print(len(l3))
print(str1,len(str1))


print(l2)
# [[2, 4, 8], [1, 3, 7]]
print(len(l2[0]))

# 리스트 값 추가
# 리스트명.append(값)
# num = [0,1,2,3,4,5,6,7]
num.append(8) # 8을 추가
num.append('숫자')
num.append([0,1,2])
print(num)

# 해보세요
# str1 ㄱ,ㄴ,ㄷ,[1,2,3]을 추가해 보세요
print(str1)
# ['a', 'b', 'c', 'd', 'e', 'f']
str1.append('ㄱ')
str1.append('ㄴ')
str1.append('ㄷ')
str1.append([1,2,3])
print(str1)

# 리스트에서 특정값 삭제
# 리스트명.remove(값)
num.remove(7)
print(num)

#str1에서 a,c,f를 삭제해보세요

print(str1)
# ['a', 'b', 'c', 'd', 'e', 'f', 'ㄱ', 'ㄴ', 'ㄷ', [1, 2, 3]]
str1.remove('a')
str1.remove('c')
str1.remove('f')
print(str1)
# ['b', 'd', 'e', 'ㄱ', 'ㄴ', 'ㄷ', [1, 2, 3]]

# 요소확인 : 내부에 포함된 요소 존재 확인
# in, not in
print( 1 in num) # > True or False
print( 10 not in num)

lan = ['영어', '한국어', '일본어', '스페인어', '중국어']
print('영어'in lan)
print('한글' not in lan)

if '일본어' in lan:
    print('일본어가 있습니다')
    
# 해보세요
tmp = [
    ['미국','영국','일본','중국','스페인'],
    ['영어','영어', '일본어','중국어','스페인어']
]

# 일본어를 출력해보세요
print(tmp[1][2])
# 중국을 대만으로 변경해보세요
tmp[0][3] = '대만'  #!!
print(tmp)
# 스페인을 이탈리아로 변경해보세요
tmp[0][-1] = '이탈리아'
print(tmp)
# # 일본부터 스페인까지 출력해보세요
print(tmp[0][2:])
# 프랑스와 프랑스어를 추가해보세요
tmp[0].append('프랑스')
tmp[1].append('프랑스어')
print(tmp)
# # 중국어를 삭제해보세요
# tmp[1].remove('중국어')
# print(tmp)
# tmp[1].remove('영어')
# print(tmp)
# tmp[1][2] = '독일어'
# print(tmp)
tmp[1].append('python')
print(tmp)