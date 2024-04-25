# stu.txt 파일을 읽어 출력하시오

# f= open('stu.txt','r',encoding='utf8')

# while True:
#     content= f.readline()
#     if content == '' : break
#     print(content,end='\n')
    
# f.close()


students = []
with open('stu.txt','r',encoding='utf-8') as f:
    while True:
        txt = f.readline()
        if txt == '': break
        t_list = txt.split(',') # csv 파일을 ,로 분리
        s_dic = { "stuNo":int(t_list[0]), "name": t_list[1], 
                 "kor":int(t_list[2]), "eng":int(t_list[3]), "math": int(t_list[4]), 
                 "total":int(t_list[5]), "avg":float(t_list[6]), "rank":int(t_list[7]) }
        # print("{},{},{},{},{},{},{}".format(*t_list))
        
        students.append(s_dic)
print(students)


# clear