# 아이디 패스워드 랜덤 10개 생성 
import random
def idpw():
    id = 'abcdefghijklmnopqrstuvwxyz'
    pw = '1234567890'
    all_idpw = []
    for i in range(10) :
        u1 = random.choice(id)
        u2 = random.choice(id)
        u3 = random.choice(id)
        u4 = random.choice(pw)
        u5 = random.choice(pw)
        u6 = random.choice(pw)
        u7 = random.choice(pw)
        uid = u1+u2+u3
        upw = u4+u5+u6+u7
        all_idpw.append([uid,upw])

    return all_idpw

# 아이디 패스워드 파일에 저장
def idpw_open(all_idpw):
    with open("all_idpw.txt",'w',encoding='utf8') as f:
        for i in range(len(all_idpw)):
            f.write(str(all_idpw[i][0])+','+str(all_idpw[i][1])+'\n')


# def log_in(success_flag,all_idpw):  # idpw 리스트
#     success_flag = 0
#     while True:
#         print('-'*50)
#         print('로그인 하세요')
#         print('-'*50)
#         id_input = input('ID를 입력하세요 >> ')
#         pw_input = input('PASSWORD를 입력하세요 (-1. 취소)>> ')
#         if pw_input == '-1': break

#         for user in range(len(all_idpw)):
#             if id_input == user[0]:             # ID와 PW 중 어디가 틀렸는지 표기하려고 한다면
#                 if pw_input == user[1]:     
#                     success_flag = 1                                                                                                                            
#                     print('로그인 되었습니다')
#                     break                   
#                 else: 
#                     print('패스워드가 맞지 않습니다. 다시 입력해 주세요')
#                     break
#             else:
#                 print('아이디가 맞지 않습니다. 다시 입력해 주세요')
#                 continue
        
#         break    # chatGPT로 검토하고 따로 떼어내서 다른 파일에서 되는 것을 확인했는데 왜 여기서는 안될까?
#     return success_flag, all_idpw

