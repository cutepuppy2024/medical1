students = [
    [1, '홍길동', 100, 100, 99, 299, 96.67,1],
        [2, '유관순', 99, 99, 98, 296, 98.67,1], 
        [3, '강감찬', 80, 80, 81, 241, 80.33,1],
        [4, '김구', 100, 100, 90, 290, 96.67,1],
        [5, '김유신', 90, 70, 50, 210, 70.0,1],]

while True:
    search = input('삭제하려는 학생의 이름을 입력하세요>>')
    # 이름찾기
    cnt = 0 # 찾은 학생의 위치
    for stu in students :
        if stu[1] == search :
            print('{} 학생을 찾았습니다'.format(search))
            break
        cnt += 1   
    if cnt == 5 :
        print('{} 학생이 없습니다'.format(search))
    print('찾은 위치:',cnt)
    del(students[cnt])
    print(students)
    print('-'*40)