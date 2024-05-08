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
             {'stuNo': 'S004', 'name': '김 구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
             {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title =['','국어','영어','수학']
cnt = len(students)+1  # 학번
while True:
    search = input("찾는 이름을 입력하세요 (0.취소)")
    chk = 0      
    if search == '0':
        break
    for s_dic in students:
        if s_dic["name"] == search:
            break
        chk += 1
    print("찾고자 하는 학생의 위치",chk)   
    
    if chk > len(students) :
        print('찾고자 하는 학생이 없습니다.')
        break

    else:
        print(f"{search} 학생을 찾았습니다")   
        while True: 
            print('[수정할 과목 선택]')
            s_input = int(input('수정하려는 과목을 선택하세요(0.취소) >>'))
            print("1.국어\t2.영어\t3.수학")
            if s_input == 1 :
                s_1 = "kor"
                print('{}수정 :'.format(s_title[s_input]))
                #해당학생의 국어성적을 출력하세요   
                print('현재 {}점수:{}'.format(s_title[s_input],students[chk][s_1]))     
                print('-'*30)            
                score = input("수정할 {}점수를 입력하세요>>".format(s_title[s_input]))
                students[chk][s_1] = score   
                # 합계수정
                students[chk]['total'] = students[chk][s_1]+students[chk]['eng']+students[chk]['math']     
                print("{}점수 : {}점으로 수정이 완료되었습니다".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])
   
            elif s_input == 2:
                s_1 = "eng"
                #함수호출
                #s_update(s_1)
                print('{}수정'.format(s_title[s_input]))
                #해당학생의 국어성적을 출력하세요   
                print('현재 {}점수:'.format(s_title[s_input],students[chk][s_1]))     
                print('-'*30)            
                score = input("수정할 {}점수를 입력하세요".format(s_title[s_input]))
                students[chk][s_1] = score   
                # 합계수정
                students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']     
                print("{}점수 : {}점으로 수정이 완료되었습니다".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])

      
            elif s_input == 3 :
                s_1 = "math"
                #함수호출
                #s_update(s_1)
                print('{}수정'.format(s_title[s_input]))
                #해당학생의 국어성적을 출력하세요   
                print('현재 {}점수:'.format(s_title[s_input],students[chk][s_1]))     
                print('-'*30)            
                score = input("수정할 {}점수를 입력하세요".format(s_title[s_input]))
                students[chk][s_1] = score   
                # 합계수정
                students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']     
                print("{}점수 : {}점으로 수정이 완료되었습니다".format(s_title[s_input],students[chk][s_1]))
                print(students[chk])

                
                

# 함수선언          
# def s_update(s_1):  # 소스코드를 동일하게 



# 모든 학생의 국어점수를 출력하시오
'''
[국어 점수]
0.홍길동:       100
1.유관순:       98
2.이순신:       88
3.김 구:        100
4.강감찬:       98
'''
for i, s_dic in enumerate(students):
    print(f"{i}.{s_dic['name']}:\t{s_dic['kor']}")
    print(i.s_dic['name'],{s_dic['kor']})
    print("{}.{}:{}".format(i,s_dic['name'],{s_dic['kor']}))



