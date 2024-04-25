# < 문자열 : idx,len,slicing, u/l/s/t >

# print('안녕'+1)  => 에러 케이스

a = '안녕'
b = 100000
c = 2000
print(b+c)
d ='1000000'
print(b+c)
print(b+int(d))  # 타입이 같아야 사칙연산이 가능

a = 1000000  # => 자릿수를 알 수 있는 방법이 없다
b = '안녕하세요. 반갑습니다. 저는 홍길동입니다' # => 문자만 길이를 알 수 있다. 리스트 처럼 인식
print(len(b)) # 문자열 길이
print(b[0]) # 안
print(b[0]) # 하
print(len(str(a)))

a = input('문자를 입력하세요')
print('현재 입력한 문자 길이 :', len(a))


a = [1234,11111,1,145,20,1323456547]
# 리스트의 각 숫자의 길이를 출력하시오
print('현재 입력한 문자 길이 :',len(str(a[0])))
for i in a :
    print('리스트 문자 길이 :',len(str(i)))

# for i in a:
#     print(len(str(i)))
    
# 짝수만 문자 길이를 출력하시오
for i in a:
    if len(str(i))%2== 0:
        # print(len(str(i)))
        print('숫자: {}, 길이: {}'.format(i,len(str(i))))
        
# 한글자씩 출력해보세요        
title = '혼자공부하는파이썬수업'
for i in title:
    print(i)
print('제목의 길이는 :{}'.format(len(title)))


print(1,2,3,4,sep='*')

title = '안녕하세요'
for i in title:
    print(i)
    
# 역순출력
for i in range(len(title)): # 5
    print(title[(len(title)-1)-i],end="")
print()   
# print('안녕하세요',reversed=True)  => 안됨

# upper : 대문자
# swapcase : 대-소문자 교환 입력
# title : 첫글자만 대문자

shape_list = ['spadE', 'diamonD', 'heart', 'clover']
for i in shape_list:
    print(i.upper())
    print(i.title())
    print(i.swapcase())
    

    