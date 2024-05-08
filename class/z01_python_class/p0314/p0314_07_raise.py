# < 예외발생, 알림: raise "" >

print('1. 학생성적입력')
print('2. 학생성적출력')
print('3. 학생성적수정')

num = int(input('숫자를 입력하세요 >>'))
if num == 1 :
    print('학생성적입력 완성')
    
elif num == 2:
    # print('김과장이 해야할 부분')
    raise "김과장에게 소스를 받아야 함"    

elif num == 3:
    # print('이대리가 해야 할 부분')
    pass


# 출력형태 참고
#   File "c:\workspace\medical1\p0314\p0314_07.py", line 12, in <module>
#     raise "김과장에게 소스를 받아야 함"    
#


# clear