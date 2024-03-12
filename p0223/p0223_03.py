# 조건문
# 1. 키가 130cm 이상만 놀이기구를 탑승할 수 있다.

height = 120
if height>= 130 :
    print("o")
else :
    print("X")

# 조건문
# 2. 나이가 10살 이상이고 키가 130 이상만 놀이기구 탑승가능
age = 11
if 10<= age and height >=130 :
    print("탑승가능")
else :
    print("탑승할 수 없습니다")
    
# 3. 비가 오면 [우산을 챙겨주세요] 아니면 [선크림을 발라 주세요] 출력
weather = '비'
if weather == '비':
    print("우산을 챙겨주세요")
else :
    print("선크림을 발라주세요")


# 4. 비 나 눈이면 [우산을 챙겨주세요]
# 아니면 [선크림을 발라주세요] 출력
weather = input("날씨를 입력해 주세요 >>")
if weather == '비' or weather == '눈':  # 각각 변수로 지정!!
    print("우산을 챙겨주세요")
else :
    print("선크림을 발라 주세요")
    