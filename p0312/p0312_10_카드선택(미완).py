import random

# 카드 종류 : SPADE, DIAMONE, HEART, CLOVER     4종류
# 카드 숫자 : A,1,2,3,4,5,6,7,8,9,10,J,Q,K       13장
# 카드 총 수 : 52장


def card_creat():
    for i in s_card:
        for j in range(13):
            cards[cnt] = {'shape': i,'num':n_card[j]}                                                 # [[s_card[i],n_card[j]]??
            cnt +=1
        print(cards)

def card_shuffle():
    random.shuffle(cards)

def card_share():
    for i in range(2):  # 사람수
        for j in range(5):
            
            
    print(input(' 남은 카드는 {}장 >>').format(len(cards)-arr_num))
    arr_num += 1

def car_print():
    print('선택한 카드는')


c_shape =  ['SPADE', 'DIAMONE', 'HEART', 'CLOVER']
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
c_number[0] = 'A'
c_number[-1] = 'K'
c_number[-2] = 'Q'
c_number[-3] = 'j'


cards = [[0]*2 for i in range(13)]
cnt = 0
arr_num = 0
p_card = [0]*2





# 사람수
while True:
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드 5장 나눠주기')
    print('4. 카드 5장 확인하기')
    print('-'*40)

    choice = int(input('원하는 번호를 입력하세요 >>'))


    if choice == 1:
        card_creat()

        
    elif choice == 2:
        card_shuffle()
        
    elif choice == 3: 
        card_share() 
        
        
    elif choice == 4: 
        car_print()
        
    else:
        print('프로그램을 종료합니다')
        break