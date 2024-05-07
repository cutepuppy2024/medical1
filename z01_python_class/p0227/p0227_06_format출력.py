# 입력 : 이름, 아이디, 비밀번호 (input)
# 5명을 입력받아서 member 리스트를 만드세요

member = [] #[[홍길동, aaa, 1111],[유관순, bbb,2222]]

# # member 리스트를
# 이름     아이디    비밀번호
# 홍길동    aaaa     1111
# 이순신    bbbb     2222

# 형식으로 출력해보세요

for i in range(5):
    name = (input('이름을 입력하세요 >>'))
    id = input('아이디를 입력하세요 >>')
    pw = input('비밀번호를 입력하세요 >>')
    m1 = [name, id, pw]
    member.append(m1)
    print(member)

print('이름\t아이디\t비밀번호') 
for i in range(len(member)):
    print('{}\t{}\t{}'.format(
        member[i][0],member[i][1],member[i][2]))  # 적용되는 수 만큼 i로
    

# print('{}\t{}\t{}'.format(
#     member[0][0],member[0][1],member[0][2]))
#     member[1][0],member[1][1],member[1][2])) ..... 