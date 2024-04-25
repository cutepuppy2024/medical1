# 학번 1000, 이름 홍길동 학과 컴퓨터공학
# 딕셔너리
student = {'학번':1000, '이름': '홍길동', '학과': '컴퓨터공학'}
 
for key in student:        # for문 : 키 값이 넘어온다
    print("{} :{}".format(key,student[key]))
    print(f'{key}:{student[key]}')
print('-'*50)

student['연락처'] = "010-0000-0000"   # 딕셔너리 안에 리스트 추가  =>리스트에서는 수정의 형태
print(student)

# 수정
student['이름'] = '유관순'  # 키 값이 있다면 value가 수정됨
print(student)

# 학과-> 화학과                         # 키 값을 찾아 수정출력
student['학과'] = '화학과'
print(student)

print(student['이름'])    # 출력하는 방법 : key 의 value값 출력, 많이 사용
print(student.get('이름'))

# print(student['성별'])    # 키값 없을 때 error
print(student.get('성별'))  # key 값 없을 때 None, 에러가 안남

if '이름' in student:
    print('이름 키값이 있습니다')
    print(student['이름'])
else :
    print('이름 키값이 없습니다')
    
if '성별' in student:
    print('성별 키값이 있습니다')
    print(student['성별'])  # 에러
else :
    print('성별 키값이 없습니다')
    

# student.keys() 딕셔너리의 모든 key를 출력
print(student.keys())    #key의 값들이 모두 리스트 타입으로 출력
print(type(student.keys()))    # type => class => 출력형태가 달라져야 한다

print(list(student.keys()))  # ['학번', '이름', '학과', '연락처'] =>리스트 형태로 바꾸려면 형변환을 해 주어야 한다.

for i in student.keys() :
    print(i)    
print('-'*50)


# student.values()  딕셔너리의 모든 value를 출력
print(student.values())  # => value 값도 class라서 형변환
print(list(student.values()))

for i in student.values():
    print(i)
    
    
# items() 튜플 형태 데이터를 리턴
print(student.items())   # 튜플형태 dict형태와 같아서 (키,값)으로 표현되지만 삭제,수정이 안된다

if '이름' in student:            # True/False로 => 없으면 출력을 하지 않도록 해야 한다!! 실제 현장에서는 error가 나게 되면 문제의 파장이 커질 수 있다
    print("키값이 있습니다")
else:
    print("키값이 없습니다")