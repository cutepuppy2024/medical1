

def cal(num1,num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    r_list[5] = num1 / num2

    return r_list 


save_list = []
while True:
    num1 = int(input('첫번째 숫자 입력 >>(0.종료)')) 
    if num1 == 0:
        break
    num2 = int(input('두번째 숫자 입력 >>'))

    r_list = cal(num1,num2)
    save_list.append(r_list)
    # save_list에 저장
    print('{},{} 결과값: {},{},{},{}'.format(*r_list))
    print(save_list)
          


        
# -------------------------------------------------------------

save_list = []
chk = 0
while True:
    num1 = int(input('첫번째 숫자 입력 >>(0.종료)')) 
    if num1 == 0:
        break
    chk += 1   
    num2 = int(input('두번째 숫자 입력 >>'))

    r_list = cal(num1,num2)
    save_list.append(r_list)
    # save_list= [*r_list]
    # save_list에 저장
    for i in range(chk):
        print(save_list[i])
    print(save_list) 
        
# 내가 푼 것



# clear




