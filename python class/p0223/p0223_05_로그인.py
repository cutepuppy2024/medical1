id = 'admin'
pwd = '1111'

uid = input('아이디를 입력해주세요 >>')
upw = input('비밀번호를 입력해주세요 >>>')


if (id == uid) and (pwd == upw) :
    print('로그인 되었습니다')
else :
    print('아이디가 일치하지 않거나 비밀번호가 일치하지 않습니다.')
    print('다시 입력해주세요')
    
# 입력한 아이디가 같으면 비밀번호가 일치하는지 비교해서
# 같으면 [로그인 되었습니다] 아니면 [비밀번호가 일치하지 않습니다]
# 입력한 아이디가 다르면 [아이디가 일치하지 않습니다]

id = 'pythonstart'
pwd = '2024py'

uid = input('아이디를 입력해주세요 >>')
upw = input('비밀번호를 입력해주세요 >>')

      
if id == uid :
    print("아이디가 일치합니다")
    if pwd == upw :
        print("비밀번호가 일치합니다. 로그인 되었습니다")
    else:
        print("비밀번호가 일치하지 않습니다.")
        print("다시 입력해 주세요")
else:  
    print("아이디가 일치하지 않습니다.")


if (id == uid) and (pwd == upw) :
    print("로그인 되었습니다.")
else :
    if pwd != upw :
        print("비밀번호가 일치하지 않습니다")
    if id != uid :
        print("아이디가 일치하지 않습니다.")
    print("다시 입력해주세요.")

    