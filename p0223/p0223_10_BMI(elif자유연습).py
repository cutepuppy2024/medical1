# 해보세요

# 성별, 키를 입력받아서
# 남자일 경우 (m) 172.5 이상이면 [평균이상] 이하면 [평균이하]
# 여자일 경우 (f) 159.6 이상이면 [평균이상] 이하면 [평균이하]
# 그 외는 [잘못 입력하셨습니다] 라고 출력해보세요

gender = input('성별을 입력하세요 (m / f) >>')
height = float(input("키를 입력하세요 >>"))

if gender == 'm' :
    if height >= 172.5 :
        print('평균이상')
    else:
        print('평균이하')
elif gender == 'f' :
    if height >= 159.6 :
        print("평균이상")
    else:
        print('평균이하')
else :
    print('잘못 입력하셨습니다')
    


#------------------------------------------------------------
# 자율학습
# BMI = 체중(kg) / 신장(m)^2 구하기

a = float(input("체중을 입력하시오 >>"))
b = float(input('신장을 입력하시오 >>'))
bmi = a/((b/100)**2)

print('BMI = {}'.format(bmi))

if bmi < 18.5 :
    print('저체중')
elif 18.5 <= bmi < 23:
    print('정상')
elif 23 <= bmi < 25 :
    print('과체증')
elif 25 <= bmi < 30 :
    print('비만 1단계')
elif 30 <= bmi < 40 :
    print('비만 2단계')
elif 40 < bmi :
    print('비만 3단계')
else:
    print('잘못 입력하셨습니다')


