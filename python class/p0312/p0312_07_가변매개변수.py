# 가변매개변수 : * => 개수를 맞추지 않아도 error가 나지 않음, 리스트 형태로 받겠다는 의미, 와도되고 안와도 되는 변수
# 딕셔너리는 키값, ** 로 가변매개변수 표시

def str_title(num,*txt):
    print('txt타입 :',type(txt))
    print(txt)
    for i in range(num):
        for t in txt:
            print(t,end='')
        print()
        
    
print()
str_title(1,'안녕','잘가','안녕하세요','반갑습니다','사랑해요') 