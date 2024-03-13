
import random

# 화면출력함수
def screen():
    print('[로또번호 맞추기 프로그램]')
    print('[1. 번호생성]')
    print('[2. 번호섞기]')
    print('[3. 로또당첨번호입력]')
    print('[4. 번호확인]')
    print('-'*30)
    choice= int(input('원하는 번호를 입력하세요 >>'))
    return choice

# 번호생성함수
def num_generate(lottoA):
    print("[ 번호생성 ]")
    # lotto = [ i for i in range(1,45+1)]  # 지역변수로 변환, 새롭게 재정의된것이라 # 출력은 []
    for i in range(45):        # lotto = [0]*45로 만들어 놓고 
        # lotto.append(i+1) 
        lottoA[i] = i+1      
    print(lottoA)   # 이것을 함수 안에 쓰면 안된다
    
# 번호섞기함수
def num_shuffle(lottoA):
    print('[ 번호섞기 ]')
    random.shuffle(lottoA)
    print(lottoA)
    
# 번호입력함수   
def num_myN(my_lotto):
    print('[로또당첨번호뽑기]')
    for i in range(6) :
        my_num = int(input(f"{i+1} 번째 로또번호를 입력하세요.>>"))
        my_lotto[i] = my_num       # my_lotto.append(f"{i+1} 번째 로또번호를 입력하세요.>>")  # 주소값을 ins한 것이라 리턴을 더 안해도 됨
    print('내가 입력한 번호 :',my_lotto,end='\t')
    print()
    
# 번호확인함수 
def num_check(lottoA,lucky_lotto,my_lotto,win_num,win_amount):       
    print('[ 번호 확인 ]')
    for i in range(6):
        lucky_lotto[i] = lottoA[i]
    print('[로또번호 : ',lucky_lotto)
    print('[내가 입력한 번호]',my_lotto) 
    
    # 몇개 맞췄는지 확인소스       
    for i in my_lotto:
        if i in lucky_lotto:
            win_num.append(i)      #append를 없애면 안됨
    print('[당첨된 번호]:',win_num)
    # 당첨금액 출력 
    print('[당첨금액]: {:,d}원'.format (win_amount[len(win_num)]))
    

    

     
        

        
            