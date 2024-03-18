# 아이디 패스워드 랜덤 10개 생성 
import random
def idpw():
    id = 'abcdefghijklmnopqrstuvwxyz'
    pw = '1234567890'
    all_idpw = []
    for i in range(10) :
        u1 = random.choice(id)
        u2 = random.choice(id)
        u3 = random.choice(id)
        u4 = random.choice(pw)
        u5 = random.choice(pw)
        u6 = random.choice(pw)
        u7 = random.choice(pw)
        uid = u1+u2+u3
        upw = u4+u5+u6+u7
        all_idpw.append([uid,upw])

    return all_idpw

# 아이디 패스워드 파일에 저장
def idpw_open(all_idpw):
    with open("all_idpw.txt",'w',encoding='utf8') as f:
        for i in range(len(all_idpw)):
            f.write(str(all_idpw[i][0])+','+str(all_idpw[i][1])+'\n')


# def log_in(success_flag,all_idpw):  # idpw 리스트
#     success_flag = 0
#     while True:
#         print('-'*50)
#         print('로그인 하세요')
#         print('-'*50)
#         id_input = input('ID를 입력하세요 >> ')
#         pw_input = input('PASSWORD를 입력하세요 (-1. 취소)>> ')
#         if pw_input == '-1': break

#         for user in range(len(all_idpw)):
#             if id_input == user[0]:             # ID와 PW 중 어디가 틀렸는지 표기하려고 한다면
#                 if pw_input == user[1]:     
#                     success_flag = 1                                                                                                                            
#                     print('로그인 되었습니다')
#                     break                   
#                 else: 
#                     print('패스워드가 맞지 않습니다. 다시 입력해 주세요')
#                     break
#             else:
#                 print('아이디가 맞지 않습니다. 다시 입력해 주세요')
#                 continue
        
#         break    # chatGPT로 검토하고 따로 떼어내서 다른 파일에서 되는 것을 확인했는데 왜 여기서는 안될까?
#     return success_flag, all_idpw

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


def main_top_print():
        print('-'*50)  
        print(' [ 학생성적처리시스템 ]') 
        print('-'*50)
        print(' 1. 학생성적입력 ')
        print(' 2. 학생성적전체출력 ')
        print(' 3. 학생성적검색 및 출력 ')
        print(' 4. 학생성적수정 ')
        print(' 5. 등수처리 ')
        print(' 6. 학생성적삭제 ')
        print(' 7. 학생성적처리내용 저장')
        print(' 0. 프로그램종료')
        print('-'*50)
        choice = int(input('원하는 작업 번호를 입력하세요 >> '))
        if not choice.isdigit():
            print('숫자를 입력하세요')
        return choice

def score_input(students,cnt):
    while True :
        print(' 1. 학생성적입력을 선택하셨습니다 ')   # 딕셔너리에 저장
        s_dic = {}
        name = input('학생의 이름을 입력하세요 (-1 : 취소)>>')
        if name == '-1': break
        kor = input('국어성적 입력 >> ')
        eng = input('영어성적 입력 >> ')
        math = input('수학성적 입력 >> ')
        total = kor + eng + math
        avg = float(f'{total/3:.2f}')
        s_dic["stuNo"] = cnt
        s_dic["name"] = name
        s_dic["kor"] = kor
        s_dic["eng"] = eng
        s_dic["math"] = math
        s_dic["total"] = total
        s_dic["avg"] = avg
        s_dic["rank"] = 1
        students.append(s_dic)
        cnt += 1
        print(students)


def score_top_print():
    print(' 2. 학생성적전체출력을 선택하셨습니다 ')
    print('-'*50)
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*50)

def all_score_print(students):
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()

def search_student(students):
    search = input('검색하고자 하는 학생의 이름을 입력해 주세요 >>')
    search_chk = 0

    for s_dic in students:
        if s_dic["name"]  == search :
            break
        search_chk += 1
    if search_chk == len(students): 
        print(f'{search} 학생이 존재하지 않습니다.')     
    else:           
        print(f'{search} 학생이 존재합니다.')


def search_score(students,search_chk):
    search_students = []
    print(' 3. 학생성적검색 및 출력 ')
    search_student(students)
    search_students.append(students[search_chk])
    all_score_print(search_students)


def stu_subject_update(students,s_title, s_input,chk,s_1):
    print("[ {} 수정 ]".format(s_title[s_input]))
    print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
    print("-"*20)
    score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
    students[chk][s_1] = score
    # 합계수정
    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
    print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
    print(students[chk])
    return s_input, chk, s_1


def stu_update(students) :
    while True:
        # 찾는 부분 프로그램 작성하시오.
        search_student(students)
        
        while True:
            print("[ 수정할 과목 선택 ]")
            print("-"*30)
            print("1.국어\t2.영어\t3.수학")
            s_input = int(input("수정할려는 과목을 선택하세요.( 0.취소 ) >> "))
            if s_input == 1:
                s_1 = "kor"
                stu_subject_update(s_input,chk,s_1)    
            elif s_input == 2:
                s_1 = "eng"
                stu_subject_update(s_input,chk,s_1)    
            elif s_input == 3:
                s_1 = "math"
                stu_subject_update(s_input,chk,s_1)    
            else:
                print("과목 수정을 취소합니다.")
                break

def rank_stu(students):
    for i,s_dic in enumerate(students):
        rank_cnt = 1  #등수처리변수
        for i_dic in students :
            if s_dic['total'] < i_dic['total']:
                rank_cnt += 1  # 현재학생의 합계보다 크면 1증가
        s_dic["rank"] = rank_cnt      
        print('등수처리가 완료되었습니다')
        print(students)     
    print('-'*40)

def stu_delete(students,success_flag,search, search_chk):
    while True:
        search_student(students)

        if success_flag == 1:
            print(f"{search} 학생을 찾았습니다") #print("{}학생을 찾았습니다".format(search))
            s_input = input('{}학생 성적을 삭제하시겠습니까?(1. 실행, 0.취소)'.format(search))
            #삭제
            if s_input != "1":
                print('삭제를 취소합니다')
                break
            else:
                del students[search_chk]
                print('{} 학생성적이 삭제 되었습니다.'.format(search))
                print(students)
        else:
            print('검색할 학생의 이름을 다시 입력해 주세요')


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
