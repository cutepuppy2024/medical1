# students = [
#     [s001, '홍길동', 100, 100, 99, 299, 96.67,1],
#     [s002, '유관순', 99, 99, 98, 296, 98.67,1], 
#     [s003, '강감찬', 80, 80, 81, 241, 80.33,1],
#     [s004, '김구', 100, 100, 90, 290, 96.67,1],
#     [s005, '김유신', 90, 70, 50, 210, 70.0,1],
#     [s006, '이순신', 100, 100, 100, 300, 300.0,1]]

students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
             {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
             {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
             {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
             {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

            
while True :
    count = input("학생전체 출력을 하시겠습니까?(1.확인, 0.취소)")
    if count == '0':
        break
    print('\t[학생성적 출력]')
    print('-'*50)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
    print('-'*50)
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key],end="\t")
        print()
            