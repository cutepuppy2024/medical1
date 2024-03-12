import operator

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grape':'포도','mango':'망고','kiwi':'키위'}  
t_list=sorted(t_dic.items(),key=operator.itemgetter(0))

print(sorted(t_dic.items(),key=operator.itemgetter(0)))   # => 많이쓴다!!
#[('apple', '사과'), ('grape', '포도'), ('kiwi', '키위'), ('mango', '망고'), ('orange', '오렌지'), ('peach', '복숭아'), ('pear', '배')]   
print(sorted(t_dic.items(),key=operator.itemgetter(1))) 
#[('mango', '망고'), ('pear', '배'), ('peach', '복숭아'), ('apple', '사과'), ('orange', '오렌지'), ('kiwi', '키위'), ('grape', '포도')]  
print(sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True)) 
#[('pear', '배'), ('peach', '복숭아'), ('orange', '오렌지'), ('mango', '망고'), ('kiwi', '키위'), ('grape', '포도'), ('apple', '사과')]
print(sorted(t_dic.items(),key=operator.itemgetter(1),reverse=True)) 
#[('grape', '포도'), ('kiwi', '키위'), ('orange', '오렌지'), ('apple', '사과'), ('peach', '복숭아'), ('pear', '배'), ('mango', '망고')]
print(t_list)


# print(t_dic.keys())
# print(t_dic.values())
# print(t_dic.items())  #튜플

# 3개의 숫자를 입력받아 순서대로 출력하시오.
# 17, 50, 12
# 12,17,50
# num1 = [0,0,0]
# for i in range(3):
#     print(i)
#     num1[i] =int(input(f'{i+1}번째 숫자를 입력하세요'))
# #    input('{}번째 숫자를 입력하세요'.format(i+1))
# num1.sort()
# print('최대값: ', max(num1[0],num1[1],num1[2]))
# print('최대값: ', max(*num1))
# print('최소값: ', min(num1[0],num1[1],num1[2]))
# print('최소값: ', min(*num1))
# print(num1)

# num = []
# n1 = int(input('첫번째 숫자 >>'))
# n2 = int(input('두번째 숫자 >'))
# n3 = int(input('세번째 숫자 >>'))
# num.append(n1)
# num.append(n2)
# num.append(n3)
# num.sort()
# print(num)
# print(num[2]) 





# a = [5,7,4,8,1,9,3,2]
# a.sort() #순차정렬
# print(a)
# print('-'*50)

# b = [5,7,4,8,1,9,3,2]
# b.sort(reverse=True)  #역순정렬
# print(b)