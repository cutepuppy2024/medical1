member = []

# 입력 : 이름, 점수 (input) ['홍길동',90]
# 총 3명의 정보를 member 리스트에 넣으세요

# for i in range(3):
#     name = input('이름을 입력하세요 >>>')
#     score = int(input('점수를 입력하세요 >>>'))
#     m1 =[name,score]
#     member.append(m1)
# print(member) #[['홍길동,90],['유관순',91],['이순신',95]


# # m =[]
# # member.append(m)
# # print(member)    각각 따로 리스트에 넣을 수 있음

member = [['홍길동', 55], ['유관순', 80], ['이순신', 90]]
# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다
# member 변수 사용, for, if

# 이름들을 먼저 출력해보자
print(member[0][0])
print(member[1][0])
print(member[2][0])
# 점수들도 출력해 보고
print(member[0][1])
print(member[1][1])
print(member[2][1])
print(member)


for i in range(3):
    if member[i][1] >=60:
        print(member[i][0],'님 합격입니다')
    else:
        print(member[i][0],'님 불합격입니다')
        
for i in range(len(member)) :
    name = member[i][0]      #변수선언
    score = member[i][1]
    print('{}님 {}점 입니다'.format(name,score))     
    if score >= 60 :
        print(member[i][0],'님 합격입니다')
    else:
        print(member[i][0],'님 불합격입니다')
         
