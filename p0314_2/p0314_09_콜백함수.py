# 콜백함수  : 매개변수로 함수를 넘겨주는 것

# 함수선언
def callback_func(h_print):
    for i in range(10):
        h_print(i)     #h_print() 함수형태를 넣음     # print('안녕하세요')      # h_print를 넣어도 됨

# 함수선언
def h_print(num):
    print('안녕하세요',num)

# 함수호출
callback_func(h_print)
  



#---------------------------------------------------------------------
# 함수호출
h_print()

# 함수를 변수에 저장
func = h_print      
# 함수 실행을 저장한것 
func = h_print()      

print(func)



# clear  