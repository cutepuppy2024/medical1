# stu.txt에 있는 성적을 읽어 오기
def stu_file_open():
    f = open("stu.txt","r",encoding='utf8')
    students = []
    while True:
        content = f.readline()
        if content == '': break
        student = content.split(',')
        s_dic = {"stuNo":int(student[0]),"name":student[1],"kor":int(student[2]),"eng":int(student[3]),
                "math":int(student[4]),"total":int(student[5]),"avg":float(student[6]), "rank":int(student[7])}
        students.append(s_dic)

    return students
def stu_file_save(students):
    f = open("stu.txt","w",endocing=('utf8'))
    while True:
        for s_dic in students:
            stuNo = s_dic["stoNo"]
            name = s_dic["name"]
            kor = s_dic["kor"]
            eng = s_dic["eng"]
            math = s_dic['math']
            total = s_dic["total"]
            avg = s_dic["avg"]
            rank = s_dic["rank"]

        f.write(f'{stuNo},{name},{kor},{eng},{math},{total},{avg},{rank}\n')
        f.close()