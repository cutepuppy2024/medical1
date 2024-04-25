# < 딕셔너리 생성 추가, 출력 >
import operator

fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}  # 딕셔너리 생성
# 딕셔너리 추가
counter["복숭아"] = 0
counter["바나나"] = 4  #딕셔너리 추가
counter["바나나"] = 1  #딕셔너리 수정
# print(counter["딸기"]) #딕셔너리에 없는 키값을 출력할 때 에러
print(counter['바나나'])
print(counter)

if "딸기" not in counter:  # 키가 존재하는지 확인
    counter["딸기"] = 0  # 키값을 만들어 주기
else :
    print(counter["딸기"])  # 키의 value값을 출력   
    
del counter["복숭아"]  # 딕셔너리 삭제
print(counter)

                                        # 출력형태
print(counter.keys()) # class type     # dict_keys(['바나나', '딸기'])
print(counter.values())                # dict_values([1, 0])
print(counter.items())                 # dict_items([('바나나', 1), ('딸기', 0)])

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list))
print(a_list.sort())   # None
