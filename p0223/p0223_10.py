# 해보세요
# 성별, 키를 입력받아서
# 남자일 경우 (m) 172.5 이상이면 [평균이상] 이하면 [평균이하]
# 여자일 경우 (f) 159.6 이상이면 [평균이상] 이하면 [평균이하]
# 그 외는 [잘못 입력하셨습니다] 라고 출력해보세요
gender = input('성별을 입력하세요 (m / f) >>')
height = float(input("키를 입력하세요  >>"))

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
    
    
#BMI = 체중(kg) / 신장(m)^2 


a = float(input("체중을 입력하시오 >>"))
b = float(input('신장을 입력하시오 >>'))
cal = input('수식을 입력하시오 >>')

if cal == '/' :
    print(a/(b**2))


