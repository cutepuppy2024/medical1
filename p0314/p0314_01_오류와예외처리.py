# < 오류와 예외처리 >

# 예외 - 프로그램 실행시 알수 없는 오류로 인한 프로그램 종료를 방지하기 위해
# 프로그램 에러 - 프로그램 실행하면서 수정을 해야 함.
# 예외처리를 하게 되면, 오류가 발생이 되어도 
# 프로그램이 종료되지 않음

# try: 프로그램에서 오류가 발생 될 것 같은 소스 
# except: 예외발생시 처리 구문 소스 
# else: 예외발생이 되지 않을 시 처리소스 
# finally : 무조건 실행되는 소스
# except Exception as e : 예외발생시 어떤 예외가 발생이 되었는지 확인 가능  # print(e)
# 예외 종류별로 except 처리 가능
# ValueError, Index, ZeroDivisionError... 등 최고부모 : Exception
# raise : 예외를 강제로 발생시킴 "메모내용"

  
# < 오류 >        
while True:
# 프로그램 구현중에 잘못된 코드 : 구문오류, 프로그램 실행 전 => 실행이 되지 않는다
    print('[리스트 출력 프로그램]')     # 런타임오류: 프로그램 실행 중에 발생하는 오류
    num = int(input('숫자를 입력하세요'))        
    a_list = [1,2,3,4,5]     
    if num.isdigit():
        if int(num) < 5:
            for i in range(int(num)):
                print(a_list[i])
        else:
            print('5보다 작은 숫자를 입력하셔야 실행이 됩니다.')
    else:
        print('숫자가 아닙니다. 숫자를 입력하셔야 합니다.')
        
#--------------------------------------------------------------------------     

       
    # < 예외처리 >     
while True:                        # try, except : 돌려보고 어디에 오류가 났는지 확인하는 도구
    print('[리스트 출력 프로그램]')   

    try:   # 오류가 발생 될것 같은 지점        
        num = int(input('숫자를 입력하세요'))  # 런타임오류: 프로그램 실행 중에 발생하는 오류
        a_list = [1,2,3,4,5]
        for i in range(int(num)):
            print(a_list[i])
    except :
            print('구문에 오류가 났습니다')
            
            
            
# clear
        
        



