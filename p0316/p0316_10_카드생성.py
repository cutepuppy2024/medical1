class Card:
    kind = ''
    number = ''
    
    def __init__(self,kind='',number=''):
        self.kind = kind
        self.number = number

# 클래스를 이용해서 52장의 카드 생성
c_list = []
kind = ["spade","diamond","heart",'clover']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(4):
    for j in range(13):
        c = Card(kind[i],number[j])
        c_list.append(c)

for i in range(52):
        print("카드출력 :",c_list[i].kind,c_list[i].number)


# 리스트를 이용해서 52장의 카드 생성
c_list = []
kind = ["spade","diamond","heart",'clover']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c = [kind[i],number[j]]
        c_list.append(c)
        
for i in range(4):
    for j in range(13):
        print("카드출력 :",kind[i],number[j])
print(c_list)
 
 
 
# 1개 변수로 선언  
kind = "spade"
number = "1"

kind2 = "heart"
number2 = "5"

kind3 = "diamond"
number = "4"


#===========================================================
        
# 클래스 출력 및 변경    
c1 = Card("spade",1)
print(f'{c1.kind},{c1.number}')

# c1에 숫자를 5로 변경하시오
c1.number =5
print(c1.kind, c1.number)


# c2 "heart","A"
c2 = Card("heart","A")
print(f'{c2.kind},{c2.number}')

# c2 kind = diamond로 변경
c2.kind = "diamond"
print(c2.kind,c2.number)






