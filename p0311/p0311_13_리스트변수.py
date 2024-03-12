def stu_update(student): # 지역변수    # 한개짜리 변수는 return이 반드시 있어야 되지만 리스트 형태는 return이 없어도 된다. 값이 많은경우 리스트가 유리
    student[0] = 2      # 자리값
    student[1] = '유관순'
    student[5] = student[2] + student[3] + student[4]
    student[6] =student[5]/3

   



# 프로그램 구현
student = [1,'홍길동',100,100,100,0,0]   # 2개 이상의 변수 주소값이 저장되어 있음 student라는 data 안에는
 

# 함수호출
stu_update(student)

print('학생1:',student)

