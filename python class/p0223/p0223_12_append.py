fruits = ['사과','복숭아','딸기','포도','배']
# 한라봉을 추가하고 싶을 때
print('추가전 리스트:', fruits)
# 리스트에 요소 추가하기
fruits.append('한라봉')
print('추가후 리스트:', fruits)

if '딸기' in fruits:
    print('딸기가 있습니다.')
else :
    print('딸기가 없습니다')
    
temp = []
print(temp)
temp.append(1)
print(temp)
temp.append(2)
print(temp)
temp.append('홍길동')
print(temp)

# 과일 리스트에 '체리' 추가하기
fruits =[]
print(fruits)
fruits.append('체리')
print(fruits)
fruits.append('귤')
print(fruits)
fruits.append('사과')
print(fruits)

# remove: 제거
# 리스트명.remove(항목의 특정값)
fruits.remove('사과')
print(fruits)

# 변수와 리스트 비교 # 2+3=5
a = 2
b = 3
c = a + b
print('{}+{}={}'.format(a,b,c)) 

l1 =[1,2,3,4,5] 
a1 =  2 # l[]
b1 =  3 # l1[]
print('{}+{}={}'.format(l1[1],l1[2],l1[1]+l1[2]))






