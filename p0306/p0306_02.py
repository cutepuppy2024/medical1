# < 딕셔너리, 리스트에 있는 값을 딕셔너리로 분류하여 카운트 / 정렬 >
import operator

fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}  # 딕셔너리 생성

for f in fruit:
    if f not in counter:  # 딕셔너리에 키가 존재하는지 확인
        counter[f] = 0  # 딕셔너리 키가 없을 때 키추가
    counter[f] += 1   # 키의 value 값 1 증가
print(counter)  # {'바나나': 6, '딸기': 10, '배': 2, '사과': 4}

#리스트는 값을 그냥 비교, 딕셔너리는 값을 비교해야 하므로 operator 사용
# 딕셔너리 정렬 = key순 : 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(0)))   
# 딕셔너리 정렬 = key순 : 역순정렬
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))  

# 딕셔너리 정렬 = value순 : 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(1)))  
# 딕셔너리 정렬 = value순 : 역순정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))  
 