import random 
c_shape =  ['SPADE', 'DIAMONE', 'HEART', 'CLOVER']
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
    
    
c_number = [1,2,3,4,5,6,7,8,9.10,11,12,13]


# 랜덤으로 2개 숫자를 뽑아서 출력하시오

random.shuffle(c_number)

s_num = random.sample(c_number,k=2)
print(s_num)

# 랜덤숫자 : 2-> 1번방에 있습니다
# 랜덤숫자 : 9-> 8번방에 있습니다
# 큰수: 9, 작은수 : 2

for i, num in enumerate(c_number):
     if s_num[0] == c_number[i]:
        print(f'랜덤숫자 {s_num[0]} {i}번 방에 있습니다') 
        if s_num[0] < s_num[1]:
            print(f'큰수{s_num[1]}, 작은수{s_num[0]}')
        else:
            print(f'큰수{s_num[0]}, 작은수{s_num[1]}')            
        
