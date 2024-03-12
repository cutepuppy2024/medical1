# 변수 3개를 만들어서 name, city, fruit
# 저의 이름은 name 입니다.
# 저는 city시에서 태어났습니다
# 저는 fruit를 좋아합니다.

name = "홍길동"
print("저의 이름은",name,"입니다")

city = "부산"
print("저는",city+"시에서 태어났습니다.")

fruit = "딸기"
print("저는",fruit+"를 좋아합니다")

str = "홍길동"
print("저의 이름은 %s입니다"%str)
str1 = "부산시"
print("저는 %s에서 태어났습니다"%str1)
str2 = "딸기"
print("저는 %s를 좋아합니다"%str2)

str = "홍길동"
str1 = "부산시"
str2 = "딸기"
print("저의 이름은 {}입니다.".format(str))
print("저는 {}에서 태어났습니다.".format(str1))
print("저는 {}를 좋아합니다.".format(str2))

# 변수 선언 -> input으로 입력을 받아서 출력
# input()
inputVal = input("입력하시오 >>")
print("입력하신 글자는 "+inputVal)


name = input("이름을 입력하세요>>")
city = input("도시를 입력하세요")
fruit = input("과일을 입력하세요")
print("저의 이름은",name,"입니다")
print("저는",city+"시에서 태어났습니다.")
print("저는",fruit+"를 좋아합니다")