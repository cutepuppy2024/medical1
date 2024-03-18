# stu 파일 읽어오기
def stu_file_open():
    with open("stu.txt","r",encoding='utf8') as stu:   # txt파일을 가지고 와서 리스트에 저장 후 딕셔너리에 저장
        students = []
        while True:
            student = stu.readline()
            if student == '' : break
            s_each = student.split()    # 각 학생을 리스트형태로
            s_dic = {"stuNo":s_each[0], "name":s_each[1], "kor":s_each[2],     # 리스트의 값들을 딕셔너리에 저장
                    "eng":s_each[3], "math":s_each[4], "total": s_each[5], 
                    "avg": s_each[6], "rank": s_each[7]}
            students.append(s_dic)
            
        return students


# 성적처리 후 파일저장
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
