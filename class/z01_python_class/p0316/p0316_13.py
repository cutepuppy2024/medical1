class Student:
    stuCount = 0
    stuNo = 0
    
    def __init__(self,name='',kor=0, eng=0, math=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        self.rank = 1
        Student.stuCount += 1
        self.stuNo = Student.stuCount
        

stu_list = []

s1 = Student("홍길동",100,90,80)
stu_list.append(s1)
print(s1.stuNo,s1.name,s1.kor,s1.eng, s1.math, s1.total, s1.avg, s1.rank)

s2 = Student("유관순",80,90,95)
stu_list.append(s2)
print(s2.stuNo,s2.name,s2.kor,s2.eng, s2.math, s2.total, s2.avg, s2.rank)

s3 = Student("강감찬",90,85,100)
stu_list.append(s3)
print(s3.stuNo,s3.name,s3.kor,s3.eng, s3.math, s3.total, s3.avg, s3.rank)


for i in range(len(stu_list)):
    print(stu_list[i].stuNo,stu_list[i].name,stu_list[i].kor,stu_list[i].eng, stu_list[i].math, stu_list[i].total, stu_list[i].avg, stu_list[i].rank)



# class Student:
#     stuCount = 0
#     stuNo = 0
    
#     def __init__(self,name='',kor=0, eng=0, math=0):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math
#         self.total = kor + eng + math
#         self.avg = float('{:.2f}'.format(self.total/3))
#         self.rank = 1
#         Student.stuCount += 1
#         self.stuNo = Student.stuCount

#     def stu_print(self):
#         print(self.stuNo,self.name, self.kor, self.eng, self.math\
#             , self.total, self.avg, self.rank, sep="\t")
#         print("학생성적 : ")   


# stu_list = []

# s1 = Student("홍길동",100,90,80)
# s2 = Student("유관순",80,90,95)
# s3 = Student("강감찬",90,85,100)



            


    



 
        
    
 


