# < 2중 for 문을 빠져나오는 방법 >

# 처음 선택해서 종료가 아니라 중간에 종료시키고 싶은 경우

# 구구단 = 이중 for 문을 사용하고 있음
# 변수를 1개를 사용해야 함.
temp = 0
for i in range(1,10) :
    # if i == 2: break
    for j in range(1,10):
        if j == 5:
            temp = 1
            break
            # 여기에서 종료하는 방법
        print(f'{i}*{j} = {i*j}')
    if temp = 1:
        break