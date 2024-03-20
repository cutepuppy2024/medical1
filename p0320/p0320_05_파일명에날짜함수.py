# input으로 입력받은 데이터를
# p_0320.txt 파일을 생성해서 저장하시오
# p_0320은 현재날짜를 사용하시오.


import datetime


now = datetime.datetime.now()

# print(now.month)
# print(now.day)
print(now.strftime("%m%d"))
str1= input("입력")
fileName = 'p_'+now.strftime("%m%d") +".txt"

f = open(fileName,"w",encoding='utf8')
f.write(str1+"\n")
   
f.close()



import datetime

# 날짜
now = datetime.datetime.now
f_name = 'p'+now.strftime("%m%d")+'.txt'
# 파일명
str1 = input("입력")

with open("","w",encoding='utf8') as f:
    f.write(str1)
    