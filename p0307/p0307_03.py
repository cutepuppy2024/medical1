# < 키 값이 없을 때 에러, if를 사용해서 묻기 >

students = {"stuNo":1,"stuName":"홍길동", "tel": "010-0000-0000",
            "gender":"male", "id":"aaa", "pw": 1111}

# nicName : 길동스

# 키 값이 없는 데이터를 가져오려고 할 때는 error
# students['stuNo'] = students['stuNo' +1] 
# print(students['studentNo'])

if "studentNo" in students:
    print('key가 있습니다')
    students['stuNo'] = students['stuNo' +1]
    print(students['studentNo']) 
else:
    print('key가 존재하지 않습니다')
    
