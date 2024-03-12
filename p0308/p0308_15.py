# < 문자열 확인 : isdigit, isalpha, isalnum, islower, isupper,isspace  >  프로그램 상 문제가 없는데 데이터 값에 문자가 있는 경우 사용

print('1234'.isdigit())  # 숫자인지 확인
print('1234a'.isdigit()) #   => False
print('abc'.isalpha())   # 영문인지 확인
print('a1bc'.isalpha())  # => False
print('abc'.islower())   # 소문자인지 확인
print('abcD'.islower())   # => False
print('ABD'.isupper())  # 대문자인지 확인
print('ABcD'.isupper())   # => False
print(' '.isspace()) #  = 문자열이 공백인지  => 빈공백을 컴퓨터는 무한대로 인식, 채워주어야 연산 및 처리가 가능하다
print("  ab c".isspace())  # => False 