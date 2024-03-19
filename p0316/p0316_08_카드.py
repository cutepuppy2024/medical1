class Card:       # 4개의 변수 : kind, number, width, height
    width = 100   # 클래스변수
    height = 200  # 클래스변수
    kind = ''
    number = ''
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200
        
        
        
# 클래스를 5개를 생성해서 kind = 'spade', number =1,2,3,4,5
# 클래스를 출력하시오   


card_list = []

for i in range(13):
    card_list.append(Card('spade',i+1))

# card_list.append(Card('spade','1'))
# card_list.append(Card('spade','2'))
# card_list.append(Card('spade','3'))
# card_list.append(Card('spade','4'))
# card_list.append(Card('spade','5'))
# card_list.append(Card('spade','6'))
# card_list.append(Card('spade','7'))
# card_list.append(Card('spade','8'))
# card_list.append(Card('spade','9'))
# card_list.append(Card('spade','J'))
# card_list.append(Card('spade','Q'))
# card_list.append(Card('spade','K'))

print("리스트 개수:", len(card_list))

for i in range(13):
    print("리스트 출력 :", card_list[i].kind, card_list[i].number)


# print("리스트 출력 :", card_list[0].kind, card_list[0].number)
# print("리스트 출력 :", card_list[1].kind, card_list[1].number)
#....
# print("리스트 출력 :", card_list[12].kind, card_list[12].number)




# c1 = Card()
# print(f'{c1.kind[0]},{c1.number[0]}')

     
        
# 52장의 카드 생성
shape = ['SPADE','DIAMOND', 'HEART', 'CLOVER']
number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
card_list = []  

for i in range(4):
    for j in range(13):
        c = Card(shape[i],number[j])   # 객체선언
        card_list.append(c)
    
for i in range(52):
    c = card_list[i]
    print("카드 출력 : ", c.kind, c.number)



