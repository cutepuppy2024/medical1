def stu_open():
    students = []
    with open('stu.txt','r',encoding='utf-8') as f:
        while True:
            txt = f.readline()
            if txt == '': break
            t_list = txt.split(',') # csv 파일을 ,로 분리
            s_dic = { "stuNo":int(t_list[0]), "name":t_list[1], 
                    "kor":int(t_list[2]), "eng":int(t_list[3]), "math": int(t_list[4]), 
                    "total":int(t_list[5]), "avg":float(t_list[6]), "rank":int(t_list[7]) }
            # print("{},{},{},{},{},{},{}".format(*t_list))
            
            students.append(s_dic)
            
    return students


# 학생성적파일 저장함수
def stu_save(students):
    students = []
    with open('stu.txt','w',encoding='utf-8') as f:
        for s in students:
            stuNo = s["stuNo"]
            name = s["name "]
            kor = s["kor"]
            eng = s["eng"]
            math = s["math"]
            total = s["total"]
            avg = s["avg"]
            rank = s["rank"]
            
        f.write(f'{stuNo},{name},{kor},{eng},{math},{total},{avg},{rank}\n')
    print('모든 내용이 파일에 저장되었습니다')
    print()                                                                                            

def stu_update():
    pass
    print()       

# clear
