students = [
    [1,"홍길동",100,100,99,299,99.97],
    [2,"유관순",100,100,99,299,99.97],
    [3,"이순신",100,100,99,299,99.97]
    ]

# 찾는 학생의 이름


# 찾고자 하는 학생찾기

while True:
    # 멈춤
    search = input('검색하고 싶은 학생의 이름을 입력하세요 .(0.취소)>>')
    chk = 0 # 찾는 정보확인
    if search == "0":
        break
    for stu in students :
        if stu[1] == search :
            print('{}의 학생정보를 찾았습니다'.format(search))
        else:
            print('찾는 학생 정보가 없습니다')   
        

    