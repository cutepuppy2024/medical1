import p0315_02

member = p0315_02.idpw()  
print(member)


# mem.txt 파일에 aaa,1111 저장하시오

# f = open('mem.txt','w',encoding=('utf8'))

# f.write('aaa,1111\n')
# f.write('bbb,2222\n')
# f.write('ccc,3333\n')

# f.close()

# print('파일이 저장되었습니다')


# f = open('mem.txt','w',encoding='utf8')

# for m in member:
#     f.write('{},{}\n'.format(m[0],m[1]))

# f.close()








# from member import*

# p = member.idpw()   # 
        
# print(p) 





# 랜덤함수를 사용하여
# 3자리 아이디를 10개 생성해서 e-list에 추가하시오

# e_list = []                      #사고의 과정 수정하기

# for i in range(10):
#     temp = random.sample(eng,k=3)
#     e_list.append(temp[0] + temp[1] + temp[2])
#     # temp1 = random.choice(eng)
#     # temp2 = random.choice(eng)
#     # temp3 = random.choice(eng)
#     # e_list.append(temp1+temp2+temp3)   #중복문자가 들어옴
# print(e_list) 


# # 4자리 패스워드를 10개 생성해서 p_list에 추가하시오

# p_list = []                      
# for i in range(10):
#     temp = random.sample(eng,k=3)
# p_list.append(temp[0] + temp[1] + temp[2])
#     # temp1 = random.choice(pw)
#     # temp2 = random.choice(pw)
#     # temp3 = random.choice(pw)
#     # temp4 = random.choice(pw)
#     # p_list.append(temp1+temp2+temp3+temp3) 
# print(p_list) 

# e_list = []                      #사고의 과정 수정하기
# member = []
# for i in range(10):
#     temp = random.sample(eng,k=3)
#     e_list.append(temp[0] + temp[1] + temp[2])
#     temp1 = random.choice(eng)
#     temp2 = random.choice(eng)
#     temp3 = random.choice(eng)
#     temp4 = random.choice(pw)
#     temp5 = random.choice(pw)
#     temp6 = random.choice(pw)
#     temp7 = random.choice(pw)
#     member.append([temp1+temp2+temp3+temp4+temp5+temp6+temp7])  
# print(member) 





