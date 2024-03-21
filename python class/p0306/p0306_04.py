# < 과일 영어 단어 맞추기 게임 만들기 >

fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grape':'포도','mango':'망고','kiwi':'키위'}  

# 한글을 출력
# 복숭아 영어로 입력하시오 => 순차적으로 출력

for f in fruits:     # 기억 꼭 하기!!
    print("키:",f, "value:",fruits[f])


answer = 0
wrong = 0

for f in fruits :    # 딕셔너리의 for 구문에서 카운터 변수는 키값
    eng_in = input("{}를 영어로 입력하세요. >> ".format(fruits[f]))      #eng_in = input("{}를 한글로 입력하세요. >> ".format(f))
    # 프로그램 하시오
    print('입력한 단어 : {}'.format(eng_in))
    if eng_in == f:
        print('정답입니다. 정답 : {}'.format(fruits[f]))
        answer += 1
        print('정답의 갯수는 {}개 입니다'.format(answer))
    else:
        print('오답입니다. 오답 : {}'.format(fruits[f]))
        wrong += 1
        print('오답의 갯수는 {}개 입니다'.format(wrong))        

print('[문제체크]',len(fruits))
print('정답:',answer)
print('오답:',wrong)    


# 각 과일에 대해 묻고
# 몇 문제를 맞추었는지

fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grape':'포도','mango':'망고','kiwi':'키위'}  
right = 0
wrong = 0
for f in fruits:
    w_fruit = input('{} 과일 이름을 영어로 입력하세요 >>'.format(fruits[f]))
    if w_fruit == f :
        print('{}는 {}로 정답입니다'.format(w_fruit,f))
        right += 1
    else:
        print('{}는 {}로 오답입니다'.format(w_fruit,f))
        wrong += 1
print('총 문제 개수 :',len(fruits))
print('정답 :',right)
print('오답 :',wrong)