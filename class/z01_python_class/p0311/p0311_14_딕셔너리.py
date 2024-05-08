def stu_update(student): # 지역변수    # 한개짜리 변수는 return이 반드시 있어야 되지만 리스트 형태는 return이 없어도 된다. 값이 많은경우 리스트가 유리
    student["stuNo"] = 2 
    student["name"] = '유관순'
    student["total"] = student['kor'] + student['eng'] + student['math']
    student['avg'] = student['total']/3

   



# 프로그램 구현
student = {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}
 

# 함수호출
stu_update(student)

print('학생1:',student)

