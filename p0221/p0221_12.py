print("안녕하세요","반갑습니다")
print(str(30)+"살 입니다")
print("Hello"*3)
print( 5 > 10)
print(0*10)
print("0"*10)
print("100+100")
print(100+100)
print("숫자는 %d"%300)
print("%d"%200)
print("%d+%d=%d"%(2,3,2+3))
print("%d%d        ,,sdjk  "%(20,10))
print("%d*%d=%d"%(2,1,2*1))
print("%d"%123)
print("%7d"%123)
print("%05d"%123)
print("%d"%123.45)
print("%f"%123.45)
print("%7.1f"%123.45)
print("%7.3f"%123.45)
print("%7f"%12.3456)
print("%.2f"%12.3456)
print("%.3f"%12.3456)
print("안녕하세요")
print("%s"%"반갑습니다")
print("%c"%'a')
print("%s"%"반갑습니다")
print("%.2f"%758.12345678)
print("%010.2f"%25.05)
print("%d"%150.15)
print("%f"%150.15)
print("%s"%150.15)
print("%d-%5d-%05d"%(123,123,123))
print("{}-{}-{}".format(123,123,123))
print("{}-{}-{}".format(1,3.14,"안녕"))
print("{}+{}={}".format(1,2,1+2))
print("오늘은 날씨가 흐림. \n내일은 날씨가 맑음")
print("오늘은 날씨가 흐림. \t내일은 날씨가 맑음")
print("철수가 말했습니다. \"영희의 생각은 어떨까?\"")
print("""\
    안녕하세요.
    반갑습니다\
             """)
str1 = "hello"
print(str1)
str2 = "world"
print(str1,str2)
print(str1+str2)
print(str1+' '+str2)


stu_no = input("숫자를 입력하세요 >>")
stu_name = input("이름을 입력하세요 >>")
kor = input("국어성적을 입력하세요 >> ")
eng = input("영어성적을 입력하세요 >> ")
math = input("수학성적을 입력하세요 >> ")
total = input("세 과목의 합계를 입력하세요 >>")
avg = input("세 과목의 평균값을 입력하세요 >>")
print("번호", "이름", "국어", "영어", "수학", "합계", "평균","등수")
print("%s"%stu_no, "%s"%stu_name, "%s"%kor, "%s"%eng, "%s"%math, "%s"%total, "%s"%avg)
print("%d+%d+%d=%d"%(str(kor),str(eng),str(math),str(kor)+str(eng)+str(math)))