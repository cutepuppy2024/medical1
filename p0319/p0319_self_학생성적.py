# stu.txt에 있는 성적을 읽어 오기
from stu_file import*

students = stu_file_open()  # students 리스트 안에 s_dic 
print(students)


# ---------------------
# 함수 부분
# ---------------------
def main_print():
    print(' [ 학생성적처리 시스템 ]')
    print('1. 학생성적입력 ')
    print('2. 학생성적전체출력 ')
    print('3. 학생성적검색 및 출력')
    print('4  학생성적수정')
    print('5. 등수처리 ')
    print('6. 학생성적삭제 ')
    print('7. 학생성적처리저장')
    print('0. 프로그램종료')
    print('-'*50)
    choice = int(input('원하는 번호를 선택하세요 >> '))
    
def stu_input(cnt):
    print('학생성적입력을 선택하셨습니다.')
    name = input('학생의 이름을 입력하세요 >> (0.취소)')
    s_dic = {}
    kor = int(input('국어성적을 입력하세요 >> '))
    eng = int(input('영어성적을 입력하세요 >> '))
    math = int(input('수학성적을 입력하세요 >> '))
    total = kor + eng + math
    avg = total/3
    s_dic["stuNo"] = cnt
    s_dic["name"] = name
    s_dic["kor"] = kor
    s_dic["eng"] = eng
    s_dic["math"] = math
    s_dic["total"] = total
    s_dic["avg"] = float(f'{avg}')
    s_dic["rank"] = 1
    students.append(s_dic)
    cnt += 1
    print(students)
    
def score_main_print():
    print('학생성적전체출력을 선택하셨습니다')
    print('-'*50)
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*50)
  
def all_score_print():
    score_main_print()
    for s_dic in students:
        for key in s_dic:
            print(s_dic[key],end ='\t')
        print()

def stu_search():
    print('학생성적검색 및 출력을 선택하셨습니다')
    search_stu = []
    search = input('검색하고자 하는 학생의 이름을 입력하세요 >> ')
    chk = 0
    for s_dic in students:
        if s_dic["name"] == search:                
            break
        chk += 1
    if chk == len(students):
        print(f'{search} 학생이 존재하지 않습니다.')
    else:
        print(f'{search} 학생이 존재합니다.')
        search_stu.append(students[chk])
        score_main_print()
        for s_dic in search_stu:
            for key in s_dic:
                print(s_dic[key],end ='\t')
            print()

def sub_cor(c_sub,chk,search):
    print(f'{s_sort[c_sub]} 수정')
    print(f'{search}의 현재 {s_sort[c_sub]} 성적은 {students[chk]['kor']}입니다.')
    cor_score = int(input(f'수정할 {s_sort[c_sub]}점수를 입력하세요 >> '))
    students[chk]['kor'] = cor_score
    students[chk]['total'] = students[chk]['kor'] + students[chk]['eng'] + students[chk]['math']
    students[chk]['avg'] = float(f'{students[chk]['total']/3:.2f}')
    print(f'{search} 학생의 {s_sort[c_sub]} 성적이 {cor_score}로 변경되었습니다.')
    print(students[chk])
    
def cor_score():
    print('학생성적 수정을 선택하셨습니다 >> ')
    while True:
        search = input('검색하고자 하는 학생의 이름을 입력하세요 >> ')
        chk = 0
        for s_dic in students:
            if s_dic["name"] == search:                
                break
            chk += 1
        if chk == len(students):
            print(f'{search} 학생이 존재하지 않습니다.')
        else:
            print(f'{search} 학생이 존재합니다.')
            while True:
                c_sub = int(input('수정하고자 하는 과목을 선택하세요 (1.국어, 2.영어, 3.수학) >>'))
                if c_sub == 1:
                    s_1 = 'kor'
                    sub_cor(c_sub,chk,search)
                elif c_sub == 2:
                    s_1 = 'eng'
                    sub_cor(c_sub,chk,search)
                elif c_sub == 3:
                    s_1 = 'math'
                    sub_cor(c_sub,chk,search)
                else:
                    print('과목수정을 취소합니다.')    
                
def rank_stu():
    print('등수처리를 선택하셨습니다')
    for i_dic in students:
        rank_cnt = 1
        for j_dic in students:
            if i_dic['total'] < j_dic['total']:
                rank_cnt += 1
        i_dic['rank'] = rank_cnt
    print(students)
 
def del_stu(): 
    while True:   
        print('학생삭제를 선택하셨습니다')
        search = input('검색하고자 하는 학생의 이름을 입력하세요 >> ')
        chk = 0
        for s_dic in students:
            if s_dic["name"] == search:                
                break
            chk += 1
        if chk == len(students):
            print(f'{search} 학생이 존재하지 않습니다.')
        else:
            print(f'{search} 학생이 존재합니다.')
            d_select = input('삭제하시겠습니까? (1.삭제, 0.취소)')
            if d_select != '1': 
                print('삭제를 취소합니다')
                break
            else:
                print(f'{search}학생의 성적을 삭제합니다')
                del students[chk]
                print('삭제가 완료되었습니다')
                print(students)


#-----------------------------------------------------------
# 메인프로그램
#-----------------------------------------------------------


# 학생성적처리시스템
cnt = len(students)+1   # 기존의 넘버의 최대값 다음 숫자로 입력하려면 cnt = max(s_dic["stuNo"] for i in s_dic)+1
s_sort = ['',"국어","영어","수학"]
while True:
    choice = main_print()

    if choice == 1:
        stu_input(cnt)
        
    elif choice == 2:
        all_score_print()

    elif choice == 3:
        stu_search()

    elif choice == 4:
        cor_score()     

    elif choice == 5:
        rank_stu()
        
    elif choice == 6:
        del_stu()
            
    elif choice == 7:
        stu_file_save(students)

    elif choice == 0:
        print('프로그램을 종료합니다')