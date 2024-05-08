import operator
foods = {'떡볶이':'오뎅',"짜장면":'단무지','라면':'김치','피자':'피클','맥주':'땅콩','삼겹살':'상추'}

# 키의 값을 출력하시오
print(foods.keys())
for key in foods :
    print(key,end='\t')
print()   
# value 값을 출력하시오
print(foods.values())
for value in foods :
    print(foods[value],end='\t')
print()
# key : value 형태로 출력하시오
for key in foods:
    print('{}:{}'.format(key,foods[key]))
    print(f'{key}:{foods[key]}')

# 정렬
sorted(foods.items(),key=operator.itemgetter(0))  #(딕셔너리명.items()(튜플형태로나타내겠다),key=operator.itemgetter(정렬기준))
print(sorted(foods.items(),key=operator.itemgetter(0))) 
print(dict(sorted(foods.items(),key=operator.itemgetter(0))))