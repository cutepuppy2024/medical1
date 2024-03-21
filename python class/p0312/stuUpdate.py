def stu_print()
    print('[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생성적수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')



def score_update(choice,s_title,stu):
    print(f'[{s_title[choice]}성적 수정]')
    print(f'현재 {s_title[choice]}점수 :',stu[choice+1])
    print('-'*30)
    stu[choice+1] = int(input('수정할 점수를 입력하세요 >>'))
    print('수정된 점수 :', stu[choice+1])
    stu[5] = stu[2] + stu[3] + stu[4]
    stu[6] = float('{:.2f}'.format(stu[5]/3))
    print(f'{s_title[choice]}성적이 수정되었습니다')
    

def stu_update(choice,s_title,stu):      
    if choice == 1:
        score_update(choice,s_title,stu)
        
    elif choice == 2:
        score_update(choice,s_title,stu)
                        
    elif choice == 3:
        score_update(choice,s_title,stu)