# 영어단어 맞추기 프로그램 만들기
words = []                         
w_noun = {'airplane':'비행기',
          'apple':'사과',
          'bakery':'빵집',
          'banana':'바나나',
          'bank':'은행',
          'bean':'콩',
          'bicycle':'자전거',
          'boat':'보트',
          'bowl':'그릇',
          'bus':'버스',
}
w_verb = {'come': '오다',
           'do': '하다',
           'feel' : '느끼다',
           'find' : '찾다',
           'give' : '주다',
           'know' : '알다',
           'leave' : '떠나다',
           'keep' : '유지하다',
           'go': '가다',
           'hear' : '듣다'
}

w_ad = { "accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의",    
}

w_title = ["", "명사","동사","형용사"]


while True :
    
    print('[영단어 맞추기 프로그램]')
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print('-'*50)
    choice = input('원하는 번호를 입력하세요. >>')

    if choice == '1':   
        print('{}를 선택하셨습니다'.format(w_title[int(choice)]))
        choice = input('퀴즈가 나갑니다. 준비되셨나요?(1.실행, 0.취소)')      
        count = 0        # right/wrong 으로 하면 되지 않는 이유는 다수의 선택에 대해 더해주고자 하는데 count에 대한 정의가 어렵다             
        if choice == '1' :
            # 퀴즈 프로그램
            # key가 영문, value가 한글
            # print(w_noun.keys())   # 전체 key
            # print(w_noun.values())  # 전체 value
            for key in w_noun :
                # print(key)              # = print(w_noun.keys())   # 전체 key
                # print(key,':',w_noun[key])
                answer = input('{} 단어의 뜻은? :'.format(key))
                if answer == w_noun[key]:
                    print('정답입니다')
                    count += 1
                else :
                    print('오답입니다. 정답은 {}'.format(w_noun[key]))    # format 형태의 답변 =>
            print('정답 갯수:',count)
                   
        else :
            print('퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다')
            
    elif choice == '2':
        print('{}를 선택하셨습니다'.format(w_title[int(choice)]))
        choice = input('퀴즈가 나갑니다. 준비가되셨나요?(1.실행, 0.취소)')
        count = 0   
        if choice == '1':
            for key in w_verb:
                answer = input('{} 단어의 뜻은?'.format(key))
                if answer == w_verb[key]:
                    print('정답입니다.')
                    count += 1
                else :
                    print('오답입니다. 정답은 {}'.format(w_verb[key])) 
            print('정답 갯수:',count)
            
    elif choice == '3' :
        print('{}를 선택하셨습니다'.format(w_title[int(choice)]))
        choice = input('퀴즈가 나갑니다. 준비가되셨나요?(1.실행, 0.취소)')
        count = 0   
        if choice == '1':
            for key in w_ad:
                answer = input('{} 단어의 뜻은?'.format(key))
                if answer == w_ad[key]:
                    print('정답입니다.')
                    count += 1
                else :
                    print('오답입니다. 정답은 {}'.format(w_ad[key])) 
            print('정답 갯수:',count)

    else :
        print('프로그램을 종료합니다')
        break

        