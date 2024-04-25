import operator

numbers = ['바나나', '바나나',
           '바나나','딸기', '배', '사과', '딸기',
           '딸기','딸기','딸기','사과','바나나', '바나나',
           '바나나','딸기', '배', '사과', '딸기',
           '딸기','딸기','딸기','사과']
counter = {}

#리스트에 있는 항목에 대한 카운터
for f in numbers :
    if f not in counter:
        counter[f] = 0
    counter[f] += 1
print(counter)
sorted(counter.items(),key=operator.itemgetter(0))
print(dict(sorted(counter.items(),key=operator.itemgetter(0))))