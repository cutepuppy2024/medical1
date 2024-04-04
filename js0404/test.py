#12,1,2월 겨울/ 3,4,5  봄, 6,7,8 여름  9,10,11 가을
#1 - 겨울입니다.

season2 = input("몇 월인지 입력하세요 >>")
season1= season2[:-1]
season = int(season1)

if 3<= season <= 5:
    print("봄입니다")
elif 6<= season <=8:
    print("여름입니다")
elif 9<= season <=11:
    print("가을입니다.")
else:
    print("겨울입니다.")