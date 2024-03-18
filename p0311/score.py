def stu_input(cnt,stu,name,s_title,students):       
        cnt += 1
        stu['stuNo'] = cnt
        stu['name'] = name
        kor = int(input(f'{s_title[1]} 성적을 입력하세요 >'))
        eng = int(input(f'{s_title[2]} 성적을 입력하세요 >'))
        math = int(input(f'{s_title[3]} 성적을 입력하세요 >'))
        stu['kor'] = kor 
        stu['eng'] = eng         
        stu['math'] = math
        total = kor + eng + math
        avg = float("{:.2f}".format(total/3))
        stu['total'] = total
        stu['avg'] = avg
        stu['rank'] = 1
        students.append(stu)

def all_p(students):
    print('-'*50)
    print('\t학번\t이름\t국어\t영어\t수학\t합계\t평균')
    print('-'*50)     
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key],end='\t')
        print()

def search_N(chk,s_name,students):
    for s_dic in students:
        if s_name == s_dic['name']:
            print(f'{chk}번방에 {s_dic['stuNo']},{s_name} 학생이 존재합니다.')
        chk += 1
        break
    if chk == len(students):
        print(f'{s_name}학생의 이름이 존재하지 않습니다')