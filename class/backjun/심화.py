# 동혁이는 오래된 창고를 뒤지다가 낡은 체스판과 피스를 발견했다.
# 체스판의 먼지를 털어내고 걸레로 닦으니 그럭저럭 쓸만한 체스판이 되었다. 하지만, 검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.
# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

#1,1,2,2,2,8

# 1) 딕셔너리

white_chess = {"K":0,"Q":1,"L":2, "B":2, "Kn":1, "F":6} # 발견한 체스

right_chess = {"K":1,"Q":1,"L":2, "B":2, "Kn":2, "F":8}

for key in white_chess:
    if white_chess[key] == right_chess[key]:
        continue
    else :
        print(f"{key}가 {right_chess[key]-white_chess[key]}개 필요함")
        
# 2) 리스트      
w_chess = [0,1,2,2,1,6]
r_chess = [1,1,2,2,2,8]
s_chess = ["K","Q","L","B","Kn","F"]

print(len(w_chess))

for i, elem in enumerate(w_chess):
    if w_chess[i] == r_chess[i]:
        continue
    else :
        print(f"{s_chess[i]}가 {r_chess[i]-w_chess[i]}개 필요함")
        

#-----------------------------------------------------------------------------

# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 1) while 구문으로
while True:
  word = input("영어단어를 입력하세요 >>")
  if word.isalpha():
    word = word.lower()
    chk = 0
    for i in range(len(word)//2):
      if word[i] == word[len(word)-i-1]:
        chk += 1
        print(word[i],chk)
      else:
        print("팰린드롬이 아닙니다")
        break
    if len(word)//2 == chk: 
      print("팰린드롬입니다")
  else:
    print("영어단어가 아닙니다. 다시 입력하세요")
    break
# 2) [::-1]
word = input("영어단어를 입력하세요 >>>")

if word[i] == word[::-i-1]:
    
    
#------------------------------------------------------------------------------
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

w1 = input("영어단어를 입력하세요")

w_list = w1.split()
count = {}

# 리스트에 있는 값이 딕셔너리의 키값
w_list[i] = 


      
        
    
            
        
    