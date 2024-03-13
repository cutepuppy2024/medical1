import lotto

lottoA = [0]*45      # 전체 45개 숫자
lucky_lotto = [0]*6    # 당첨번호 6개 숫자      1,20,30,40,41,45
my_lotto = [0]*6       # 내가 입력한 6개 숫자   1,20,21,23,25,44
win_num = []        # 당첨된 번호            1,20
win_amount = [0,0,1000,10000,1000000,100000000,1000000000]  # 당첨금액


while True: 
    # 화면출력함수 호출 
    choice = lotto.screen()  
    if choice == 1:    # 번호생성과 함수호출
        lotto.num_generate(lottoA)
        
    elif choice == 2:
        lotto.num_shuffle(lottoA)  # 변호섞기함수 호출
             
    elif choice == 3:
        lotto.num_myN(my_lotto)   # 번호입력함수 호출
        
    elif choice == 4:
        lotto.num_check(lottoA,lucky_lotto,my_lotto,win_num,win_amount)
        win_num = []  # 초기화