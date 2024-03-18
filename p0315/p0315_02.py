
# 4자리 패스워드를 10개 생성해서 p_list에 추가하시오.


# import random

# eng = "abcdefghijklmnopqrstuvwxyz"
# pw = "1234567890"

# member = [['aaa',1111]]
# e_list = []
# p_list = []

# 1. e_list, p_list를 각각 생성하여 member 리스트에 append
# for i in range(10):
#     temp = random.sample(eng,k=3)
# #  e_list.append(temp) : 이 때는 한 문자씩 => 각문자를 1개의 문자 취급 ex) ['m', 'f', 'z']
#     temp1 = random.choice(eng)
#     temp2 = random.choice(eng)
#     temp3 = random.choice(eng)
#     e_list.append(temp[0] + temp[1] + temp[2])        
# print(e_list)

# for i in range(10):
#     temp = random.sample(pw,k=4)
#     temp1 = random.choice(pw)
#     temp2 = random.choice(pw)
#     temp3 = random.choice(pw)
#     temp4 = random.choice(pw)
#     p_list.append(temp[0]+temp[1]+temp[2]+temp[3])
# print(p_list)

# for i in range(10):
#     member.append([e_list[i],p_list[i]])
# print(member)



# 2. for문을 1번 사용하여 member 리스트 출력 
# for i in range(10):
#     temp_i = random.sample(eng,k=3)
#     temp_p = random.sample(pw,k=4)
    
#     temp_i1 = random.choice(eng)
#     temp_i2 = random.choice(eng)
#     temp_i3 = random.choice(eng)
#     temp_p4 = random.choice(pw)
#     temp_p5 = random.choice(pw)
#     temp_p6 = random.choice(pw)
#     temp_p7 = random.choice(pw)
#     # member.append([temp1+temp2+temp3,temp4+temp5+temp6+temp7])  # temp를 2개의 이름으로 나누지 않아도 됨
    
#     tt1 = temp_i1+temp_i2+temp_i3
#     tt2 = temp_p4+temp_p5+temp_p6+temp_p7  
#     member.append([tt1,tt2])   
# print(member)



# 3. 함수적용
import random
def idpw():
    eng = "abcdefghijklmnopqrstuvwxyz"
    pw = "1234567890"
    member = [['aaa','1111']]
    for i in range(10):
        temp1 = random.choice(eng)
        temp2 = random.choice(eng)
        temp3 = random.choice(eng)
        tt1 =temp1 + temp2 + temp3
        temp4 = random.choice(pw)
        temp5 = random.choice(pw)
        temp6 = random.choice(pw)
        temp7 = random.choice(pw)
        tt2 = temp4+temp5+temp6+temp7
        member.append([tt1,tt2])
    return member

member = idpw()
print(member)






# 내가 혼동했던 것은 왜?