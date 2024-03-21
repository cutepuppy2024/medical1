# < 카드게임 - 선택 >

# card_list = [{'shape':'spade','num':'A'}, 
#             {'shape':'spade','num':2},
#             {'shape':'spade','num':3},,...
#             ]
# card_list = [['shape':'A'], 
#             ['shape':2],
#             ['shape':3],,...
#             ]
card_list = []
shape_list = ["spade",'diamone','heart', 'clover']
num_list = [0]*13
# for i in range(1,14):
#     num_list[i-1] = i
# num_list[0] ='A'
# num_list[10] ='J'
# num_list[11] ='Q'
# num_list[12] ='K'
# print(shape_list)
# print(num_list)  # => 카드모양/숫자 완성


import random
# 카드 1세트를 구현 : 52장
# card_list = [[0]*14 for i in range(4)]
# print(card_list)
# print(' ',0,1,2,3,4,5,6,7,8,9,10,11,12,sep=('\t'))
# for i in shape_list:
#     print(i,end='\t')
#     for j in num_list:
#         print(j,end='\t')
#     print()
#  #   => 내가 하려고 했던 것은 4*13 2차원 배열을 한다음 리스트로 출력 : 복잡한 접근
    
# 카드 1세트를 구현 : 52장  
card_list = [[0]*2 for i in range(52)]   # => 2개의 항목을 만족하는 리스트 52개를 만듬 => 딕셔너리로 만들기 쉬울듯
cnt = 0  
for i in shape_list:
    for j in range(13):
        card_list[cnt] = [i,num_list[j]]
        cnt += 1

# 카드를 랜덤섞기       
random.shuffle(card_list)
print(card_list)

arr_num = 0
while True:
    print('1. 카드 1장 뽑기')
    print('2. 카드 5장 뽑기')
    print('0. 종료')
    c_num = int(input('번호를 선택해 주세요'))
    print('현재 남은 카드 :',len(card_list)-arr_num)
    if c_num == 1:
        print(card_list[arr_num])  # 0 / 6
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print(card_list[arr_num]) # 1,2,3,4,5 / 7,8,9,10,11 /
            arr_num += 1

       

