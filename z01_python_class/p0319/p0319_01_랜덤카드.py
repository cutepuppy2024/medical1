# 클래스 선언 - 설계도
import random    
class Card:
    kind = ""
    number = ""
    
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number

    def random_one():
        num = random.randint(0,51)
        print("랜덤카드1장 :",num, card_list[num].kind, card_list[num].number)
        return card_list[num]
        


# 52장의 카드    
kind_list = ["spade", "diamond", "heart", "clover"]
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = []


# 52장의 카드 생성
for i in range(4):
    for j  in range(13):
        card_list.append(Card(kind_list[i],number_list[j]))
        
for i in range(52):
    print("카드 :", card_list[i].kind, card_list[i].number)


# 랜덤으로 1장 뽑기 출력
c = Card.random_one()



# 중복을 하지 않고, 랜덤카드 5장을 뽑으시오
# 1) 0- 51 순차적으로 정렬(정렬섞기) 순차적으로 뽑으면 됨
print("1.card_list shuffle")
random.shuffle(card_list)
for i in range(5):
    print("랜덤섞기 카드 :", card_list[i].kind, card_list[i].number)

# 2) 5장을 랜덤으로 뽑으면 됨
print("2.ran_list sample")   
ran_list = random.sample(card_list,k=5)
for i in ran_list:
    print("랜덤섞기 카드 :", i.kind,i.number)
   

# 3) temp_list 저장장소를 1개 만들고, 랜덤뽑기 1장의 카드를 저장장소의 리스트와 비교
print("3.temp_list sample")   
temp_list = []
print("개수 :", len(temp_list))

cnt = 0
while True:
    if cnt == 5: break
    for i in temp_list :
        c = Card.random_one()
        if c.kind == i.kind and c.number == i.number: # 같은 카드가 있으면 다음으로 진행
            continue          
        
    # 중복카드가 없으면 추가
    temp_list.append(c)
    cnt += 1
    for i in temp_list:
        print("랜덤1장 뽑기 카드 :", i.kind, i.number)

# -----------------------------------------------------------------------------------------       

def random_one():
    num = random.randint(0,51)
    # print("랜덤카드1장 :",num, card_list[num].kind, card_list[num].number)
    return card_list[num]

print("3.temp_list sample")   
temp_list = []
cnt = 0
while True:
    if cnt == 5: break # 랜덤뽑기 카드가 5장일경우 종료
    c = random_one() # 랜덤카드 1장을 뽑기
    for i in temp_list:
        if c.kind == i.kind and c.number == i.number: # 같은 카드가 있으면 다음으로 진행
            continue
    # 중복카드가 없으면 추가
    temp_list.append(c)
    cnt += 1
for i in temp_list:
    print("랜덤1장 뽑기 카드 : ",i.kind,i.number)





# clear
        
