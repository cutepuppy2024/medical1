# 빈 리스트 생성
# [미국, 영국, 일본, 중국] 만들기
cont = []

c1 = input('나라를 입력해 주세요 >>')
c2 = input('나라를 입력해 주세요 >>')
c3 = input('나라를 입력해 주세요 >>')
c4 = input('나라를 입력해 주세요 >>')


# 1. 각변수를 리스트 안에
cont =[c1,c2,c3,c4]
print(('방법1 :', cont))

# 2. append 사용
contA =[]
contA.append(c1)
contA.append(c2)
contA.append(c3)
contA.append(c4)
print(('방법2 :', contA))

# format 사용하여 출력하기
print('{}-{}-{}-{}'.format(c1,c2,c3,c4))
print('{}-{}-{}-{}'.format(contA[2],contA[0],contA[1],contA[3]))  # 리스트의 방번호 사용 및 순서 바꾸기



f = [] #과일리스트
# 내가 입력한 과일들로 리스트를 채워보세요 과일 3개 이상
a1 = input('첫번째 과일을 입력해 주세요 >>')
a2 = input('두번째 과일을 입력해 주세요 >>')
a3 = input('세번째 과일을 입력해 주세요 >>')
           
f = [a1,a2,a3]
print(f)

f1 = []
f1.append(a1)
f1.append(a2)
f1.append(a3)
print(f1)

print('{}-{}-{}'.format(a1,a2,a3))

print('내가 좋아하는 과일은 {},{},{}입니다'.format(f[2],f[1],f[0]))
print(f1[0])



