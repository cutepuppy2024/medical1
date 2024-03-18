from practice import*


# idpw 생성
all_idpw = idpw()

# 생성된 idpw 저장
idpw_open(all_idpw)
print(all_idpw)
     
# 로그인 후 학생성적시스템에 들어갈 수 있도록 하기
s_title = ['','국어','영어','수학']
while True:
    print('-'*50)
    print('로그인 하세요')
    print('-'*50)
    id_input = input('ID를 입력하세요 >> ')
    pw_input = input('PASSWORD를 입력하세요 (-1. 취소)>> ')
    if pw_input == '-1': break
    success_flag = 0
    for user in range(len(all_idpw)):
        if id_input == user[0] and pw_input == user[1]:     
                success_flag = 1                                                                                                                            
                print('로그인 되었습니다')
                break    
        
        if success_flag == 1:
        # 학생성적파일 가지고 딕셔너리에 저장하기
            students = stu_file_open()
            cnt = max(s_dic['stuNo'] for s_dic in students)+1

            while True:           
                choice= main_top_print()

                if choice == 1:
                    score_input(students,cnt)

                elif choice == 2:
                    all_score_print(students)
                                                    
                elif choice == 3:
                    search_score(students)

                elif choice == 4:
                    stu_subject_update(students, s_title, s_input, chk, s_1)
                    stu_update()


                elif choice == 5:
                    rank_stu(students)
                    
                elif choice == 6:
                    stu_delete(students)
                                             
                elif choice == 7:
                    stu_save(students)

                elif choice == 0:
                    print(' 0. 프로그램종료 ')
                    
                else:
                    print('선택된 서비스가 없습니다') 
                    break   


    else:
        print('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력해 주세요')
        continue
        
    break  










          


        

























