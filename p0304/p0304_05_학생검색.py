students = [
    [1,"홍길동",100,100,99,299,99.97],
    [2,"유관순",100,100,99,299,99.97],
    [3,"이순신",100,100,99,299,99.97]
    ]


# 찾고자 하는 학생찾기
while True:
    # 멈춤
    search = input('검색하고 싶은 학생의 이름을 입력하세요. >> ')
    chk = 0 # 찾는 정보확인
    count = 0
    if search == "0":
        break
    for stu in students :
        if search in stu:
            chk = 1 # 찾는 정보확인
            break
        count += 1 # 못찾았을 때 반복되면서 +1, for 구문 반복
    if chk == 1:
        # 전체학생 정보출력
        print('[학생성적 출력]')
        print('{}의 학생정보를 찾았습니다'.format(search))
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        for i in students[count] :
            print(i,end='\t' )
        print()
    else:
        print('찾는 학생 정보가 없습니다')
      
