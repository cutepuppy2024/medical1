all_idpw = [['abc','1111'],['acb','2222']]
success_flag = 0
while True:
    print('-'*50)
    print('로그인 하세요')
    print('-'*50)
    id_input = input('ID를 입력하세요 >> ')
    pw_input = input('PASSWORD를 입력하세요 (-1. 취소)>> ')
    if pw_input == '-1': break


    for user in all_idpw:
        if id_input == user[0]:             # ID와 PW 중 어디가 틀렸는지 표기
            if pw_input == user[1]:     
                success_flag = 1                                                                                                                            
                print('로그인 되었습니다')
                break                   
            else: 
                print('패스워드가 맞지 않습니다. 다시 입력해 주세요')
        else:
            print('아이디가 맞지 않습니다. 다시 입력해 주세요')
    if user == len(all_idpw):
        break

if success_flag == 1:
    print('학생성적시스템')