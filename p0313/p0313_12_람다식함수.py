# 람다식함수 = 무명함수

# def sum(num1,num2):
#     return num1 + num2
# print(sum(10,20))

# a = lambda num1,num2 : num1 + num2   #리턴의 결과값이 하나이기 때문, 잘쓰지 않고 함수를 변수에 할당해야 할 때만 사용
# print(a(10,20))


# # 재귀함수 : 자기자신을 호출 => 속도느림, for문 사용하면 되어서 잘 쓰지 않음 팩토리얼에서 많이 사용

# def count(num):
#     if num>= 1:
#         print(num,end=' ')
#         count(num-1)
#     else:
#         return
    
# count(10) 


def count1(num):
    for i in range(len(num),0,-1):
        return num
        
num = count1(num)   # 리턴받는 함수 = 매개변수
print(num)