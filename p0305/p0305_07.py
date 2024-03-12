aa = [[1,[3,4,5],3,4],[5,6],[7,8,9]]
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
a = [1,2,3,4,5]
for i in a:
    print(i)
print("-"*50)
for i in aa:
    for j in i:
        print(j)
print("-"*50)
for i in aaa:
    for j in i:
        for k in j:
            print(k)
print("-"*50)           
for i in aa:                  # 배열이 있는지 여부를 물어봐야 한다.  => if
    for j in i:
        if j != list :
            print(j)
        else :
            for k in j:
                print(k)