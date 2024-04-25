# a = ['새우깡',90,1200]
# product ={"name":'새우깡','무게':90, '금액':1200}    # 딕셔너리{키:값(value)}로 구성되어 있음
# students = [1,'홍길동', 100,100,100,99]

# 리스트 대괄호, 출력 idx 번호를 사용해서 출력

products = ['새우깡',90,1200]
print(products[0])

#딕셔너리 중괄호, 출력 key를 사용해서 출력
students = {"stuNo":1, "name":"홍길동","kor":100, "eng":100, "math":100, "scie":99}   #키 값을 알면 value 값을 알 수 있도록 정의내려져 있다
print(students['stuNo'])  #1 =>value 값이 출력

students['총합'] = 399 #[키]= 값
print(students)

