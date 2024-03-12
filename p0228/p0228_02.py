# list
# 변수명 = [요소1, 요소2,...., 요소n]
# bool, int, float, string type 들이 요소로 들어갈 수 있다
# [] 리스트 자체도 요소로 들어갈 수 있다.

fruits = ['딸기', '사과', '배', '포도', '한라봉']
# 사과를 출력, 접근
f1 = fruits[1]
print(f1)
# 수박을 추가 ; 리스트변수명.append(값)
fruits.append('수박')
print(fruits)

# if - list
if '귤' in fruits:
    print('귤이 있습니다')
else:
    print('귤이 없습니다')
    
    
for f in fruits:  # 변수 in 리스트명 :
    print(f)

for n in [100,200,300,400]:  # 리스트자체를 리스트명의 자리에 쓸 수도 있음
    print(n)
    
for i in range(len(fruits)):  # 리스트의 길이만큼 i를 1씩 증가해라
    print(i)
    print(fruits[i])
    
num =[[1,2,3],[4,5,6],[7,8,9]]
#        0       1       2
#      0 1 2   0 1 2   0 1 2
# 1,4,7을 출력을 하고 싶다.
print(num[0][0],num[1][0],num[2][0])

for i in range(len(num)):  # for i in range(3) i = 0,1,2
    print(num[i][0])
    
    
    
# 해보세요  >>
con = ['미국','영국','일본','중국','스페인']
lang = ['영어','영어','일본어','중국어','스페인어']

# 각각의 리스트에 프랑스, 프랑스어를 추가해보세요
con.append('프랑스')
lang.append('프랑스어')
print(con)
print(lang)
# for 문을 사용해서 다음과 같이 출력해보세요
# 미국은 영어를 사용합니다
# 영국은 영어를 사용합니다.
#.... 프랑스는 프랑스어를 사용합니다.

for i in range(len(con)):
    print(con[i]+'는'+lang[i]+'를 사용합니다') 
    # print('{}는 {}를 사용합니다'.format(con[i],lang[i])) # format에 위치를 입력해서 숫자가 0부터 증가한다는 것을 확인해보고 i로 변환해 볼 수 있다.
    

