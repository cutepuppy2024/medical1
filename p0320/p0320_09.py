print(range(10))
a = range(10)
print(a)

print(list(range(10)))

print([i for i in range(10)])

for i in range(10,1-1,-1):
    print(i)
    
#---------------------

a_dic = {
    "a":1,
    'b':2,
    "c":3
}

for key in a_dic:
    print(a_dic[key])
    
for key in a_dic.keys():
    print(key)
    
for value in a_dic.values():
    print(value)
    
for k,v in a_dic.items():
    print(k,v)