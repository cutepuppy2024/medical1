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
        if id_input == user[0]:             # ID와 PW 중 어디가 틀렸는지 표기하려고 한다면
            if pw_input == user[1]:     
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
            print('패스워드가 맞지 않습니다. 다시 입력해 주세요')
            break
    else:
        print('아이디가 맞지 않습니다. 다시 입력해 주세요')
        continue
        
    break  





It seems like you're attempting to implement a program that allows users to log in and access a student grading system. However, it looks like there are a few issues and improvements that can be made to your code. Let's address them step by step:

Indentation Error: There's an indentation error in your code. The part where you're checking success_flag should be indented properly.

Comparison with User Input: When comparing the input ID and password with those stored in all_idpw, you need to compare with the ID and password pairs within the list, not with the index.

Use of Functions: It seems like you're calling some functions (idpw(), idpw_open(), stu_file_open(), etc.), but the definitions of these functions are not provided in your code snippet. Make sure these functions are defined and properly implemented.

Infinite Loop Issue: Your code might result in an infinite loop if the user repeatedly inputs incorrect credentials. Consider adding a mechanism to limit the number of login attempts.

Logical Errors: There might be logical errors in your code flow. For instance, after successfully logging in (success_flag == 1), you directly proceed to handle student data operations without a loop to keep the user engaged. You might want to reconsider the structure of your code to ensure smooth user interaction.

Here's a revised version of your code addressing some of these issues:


from practice import *

# idpw 생성
all_idpw = idpw()

# 생성된 idpw 저장
idpw_open(all_idpw)
print(all_idpw)

# 로그인 후 학생성적시스템에 들어갈 수 있도록 하기
s_title = ['', '국어', '영어', '수학']
login_attempts = 3

while login_attempts > 0:
    print('-' * 50)
    print('로그인 하세요')
    print('-' * 50)
    id_input = input('ID를 입력하세요 >> ')
    pw_input = input('PASSWORD를 입력하세요 (-1. 취소)>> ')

    if pw_input == '-1':
        break

    success_flag = False

    for user_id, user_pw in all_idpw:
        if id_input == user_id and pw_input == user_pw:
            success_flag = True
            print('로그인 되었습니다')
            break

    if success_flag:
        # 학생성적파일 가지고 딕셔너리에 저장하기
        students = stu_file_open()
        cnt = max(s_dic['stuNo'] for s_dic in students) + 1

        while True:
            choice = main_top_print()

            if choice == 1:
                score_input(students, cnt)

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
                break

            else:
                print('선택된 서비스가 없습니다')

    else:
        login_attempts -= 1
        print(f'로그인에 실패하였습니다. {login_attempts}번의 시도 기회가 남았습니다.')

if login_attempts == 0:
    print('로그인 시도 횟수를 초과하였습니다. 프로그램을 종료합니다.')





          


        

























