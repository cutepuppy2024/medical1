import operator
numbers =[1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}
# counter['1'] = 2  # {'1': 2, '2': 1}
# counter['2'] = 1
# print(counter)

for number in numbers:
    if number not in counter:   # counter라는 딕셔너리에 키값이 없으면
        counter[number] = 0  # counter['1'] = 2  # 딕셔너리에 추가

    counter[number] += 1 # 딕셔너리에 1을 증가
# 많이 나온 숫자로 정렬(오름차순)   
print(dict(sorted(counter.items(),key=operator.itemgetter(1))))
sorted(counter.items(),key=operator.itemgetter(0))
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
# print(counter)  # {1: 0, 2: 0, 4: 0, 6: 0, 3: 0, 7: 0}