# if- else
# if - elif - else

# if 조건문1 :  #필수문구
#    실행문1
    
# elif 조건문2 :  안써도 되지만, 새로운 조건문을 추가할 수 있다는 장점/ if가 참이 아니라면 하나 더 사용해서 추가, elif에서도 참이 아니면 else로
#      실행문2
# else:
#     실행문3
    
# 조건문1이 참이면 실행문1 실행 후 종료
# 조건문1이 거짓이고 조건문2가 참이면 실행문2 실행후 종료
# 조건문1, 조건문2가 거짓이면 실행문3 실행 후 종료

weather = '비'
if weather == '비':
    print('비가 오네요 우산을 챙겨주세요')
elif weather == '눈':
    print('눈이옵니다. 조심하세요')
else :
    print('선크림을 발라주세요')
    
    
# 변수가 양수이면 양수, 음수이면 음수, 0이면 0이라고 출력해보세요
num = -10

if num > 0:         # 모든 조건을 if로 사용해도 됨
    print("양수")
elif num == 0 :
    print('0')
else:
     print("음수")

# 돈이 만원이상 [택시를 탄다] 이천원이상 [버스를 탄다]
# 천원이상 [따릉이를 빌린다] 나머지 [걸어간다]
money = int(input("돈을 입력하세요 >>> "))

if money >= 10000 :
    print("택시를 탄다")
elif money >= 2000 :
    print("버스를 탄다")
elif money >= 1000 :
    print("따릉이를 탄다")
else :
    print("걸어간다")