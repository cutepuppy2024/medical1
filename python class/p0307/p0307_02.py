# < 리스트, 딕셔너리 비교 >

students = {"stuNo":1, "stuName":"홍길동","kor":100}
students["eng"] = 100   # => 없는 키 : 추가  / 있는 키 : 수정
print(students)
students['kor'] = 50
print(students)
del students['stuName']
print(students)

print(students.keys())
print(list(students.keys()))  # => 형변환 list, dict, int, float, str
# print(dict(students.keys()))
print(students.values())
print(students.items())  # tuple 형태는 리스트 형태로 출력되며, 수정삭제 불가능



list = [1,2,3]
list.append(4)
print(list)
del list[0]
print(list)
list[0] =100
print(list)
# list[3] = 1000
# print(list)    => error  // 전체 다 지우고 싶으면 clear