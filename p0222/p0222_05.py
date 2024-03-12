# 국어, 영어, 수학 점수를 입력받아서 평균을 출력하세요
# 출력 : 평균은 : 95점 입니다.
# 변수 : kor, eng, math


# 변수 선언해서 출력 => 풀이  : 틀린이유 - 변수 사칙연산 이해부족, 문자열로 바꿨기 때문
kor = 100
eng = 90
math = 80
avg = (kor+eng+math)/3
print("평균은 :{}점 입니다".format(avg))

# 3가지 점수를 입력받아서 출력
kor = input("국어 성적을 입력하세요 >>")
eng = input("영어 성적을 입력하세요 >>")
math = input("수학 성적을 입력하세요 >>")
kor = int(kor)
eng = int(eng)
math = int(math)
avg = (kor+eng+math)/3
print("평균은 :{}점 입니다".format(avg))


