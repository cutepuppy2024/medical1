# numbers에 있는 숫자들이 몇번 나왔는지
# 딕셔너리로 출력하시오

import operator
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

for i in numbers:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1
print(counter)
print(list(sorted(counter.items(),key=operator.itemgetter(0))))
print(list(sorted(counter.items(),key=operator.itemgetter(0),reverse=True)))
        

arrays = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]
a_dic = {}

import operator
for array in arrays:   # 보통 이런 형태로 많이 사용한다
    if array not in a_dic:   
        a_dic[array] = 0
    a_dic[array] += 1
print(a_dic) 
print(list(sorted(a_dic.items(),key=operator.itemgetter(0))))

