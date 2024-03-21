# 리스트에 1,25까지 숫자를 리스트에 입력하시오.
# [1,2,3,4,5,6,7,8,9.....25]
a= []
for i in range(26):
    a.append(i+1)
print(a)

# 1부터 25까지 2차원 리스트 생성
#[[1,2,3,4,5],[6,7,8,9,10],....,[21,22,23,24,25]]     => 문제를 어떻게 처리할 것인가 : 로직- 5의배수, tool- append, if구문

b = [] 
b_i = []
for i in range(0,25):
    if (i+1)%5==0:
        b_i.append(i+1) #[1,2,3,4,5]
        b.append(b_i)
        b_i=[]                                    # => 2차원 리스트화  !!
    else:
        b_i.append(i+1) #[1,2,3,4]
print(b)
print("-"*40)



# b = []
# for i in range(5):
#     i += 1

a= []                 
b_a =[]                                    # 내가 생각한 것은 넘버가 1개씩 더해지면서 5개까지의 숫자로 이루어진 2차원리스트가 생기면 다시 새로운 2차원리스트를 생성하도록 하는 것
for j in range(26):                          #    => 숫자가 1씩 더해지도록 한다, 불가능? 
    j += 1
    len[b]
    b_a.append(j) 
    if len(b_a) == 5:
        print(b_a)
        break
b_a = []      
print(a)


