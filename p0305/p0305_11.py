# student =['k1','k2','k3']
students = []         
count = 1
# 학번, 이름, 국어, 영어, 수학, 합계, 평균 입력하는 프로그램
while True:
    chk = input("학생성적을 추가하시겠습니까?(1.추가, 0.취소)")
    if chk == '1':
        student = {}    # 리스트와 딕셔너리 두가지 모두
        # 프로그램을 구현하시오
        stuNo = "K" + "{:03d}".format(count)  # 'K' +str(count)  => format :  string으로 만들겠다는 의미/ , 가 들어가면 문자,앞에 0이 붙는다는 것은 문자라는 의미(int면 앞에0이 붙지 않는다)
        name = (input("이름을 입력하세요 >>"))
        kor = int(input('국어점수 >'))
        eng = int(input('영어점수 >'))
        math = int(input('수학점수 >'))
        total = kor + eng + math
        avg = '{:.2f}'.format(total/3) # 계산할 수 없다  => float으로

        student['stuNo'] = stuNo
        student['name']=name
        student['kor']=kor
        student['eng']=eng
        student['math'] =math
        student['total']=total        
        student['avg'] =avg
        students.append(student)
        print("[학생정보내역]")
        for k in student.keys():
            print('{}:{}'.format(k,student))
        print('*'*50)
        print('학생 1명이 추가되었습니다')
        count += 1
    else :
        print('학번추가를 종료합니다')



