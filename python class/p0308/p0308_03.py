# < 2차원 리스트 생성방법 >
# [
#    [0],[0],[0].... 52개를 생성하시오
# ]

# 1차원 리스트 생성방법
#[0,0,0,0,0,0 .... 52개를 생성하시오] 
a_list = [0]*52
c_list = [0 for i in range(52)]

b_list = []
for i in range(52):
    b_list.append(i)
    
print(a_list)
print(b_list)
print(c_list)


# 2차원 리스트 생성방법
# => 복사
aa =[[0]*1]*52  # 얕은 복사이기에 쓸 수 없음
aa[0][0] = 1
aa[51][0] = 10
print(aa)  # => 전체가 다 바뀐다


# => 컴프리헨션을 쓰면 가능
bb = [[0]*2 for i in range(52)]
bb[0][0] = 1
bb[51][0] = 10
print(bb) 

# =>append
cc = []
for i in range(52):
    dd = []
    for i in range(2):
        dd.append(0)
    cc.append(dd)
print(cc)