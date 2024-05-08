# split()   # 문자열 분리 (),(':'),splitlines(),join('')

hobby = '게임,골프,독서'

# 리스트 타입 3개로 분리 
print(hobby.split())   # ['게임,골프,독서']
print(hobby.split(','))   # ['게임', '골프', '독서']

['게임', '골프', '독서']

h_data = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"  # csv 파일형태 
# print(h_data.split(','))  ['2023-10-23', '1', '강원도 강릉시', '강릉동인병원', '383', '21', '033)651-6167', '강릉대로419번길 42', '종합']
h_list = h_data.split(',')
print('병상수 :',h_list[4])      

a_data = "2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split('/')
print('병상수 :',a_list[4])   

# splitlines() => 엔터, \n

# 
ss = '%'  #%로 문자분리
print(ss.join('파이썬'))  

s_date = "2023/10/23"
s_date_list= s_date.split('/')
print(s_date_list)

s_time = "2023:03:08:16:48:00"
s_time_list = s_time.split(':')
print(s_time_list)


today = '2024/03/08'
# 10년 후의 날짜를 출력하시오
today_list =today.split('/')
today_list[0] = int(today_list[0])+10

print(today2 ="{}/{}/{}".format(today_list[0],today_list[1],today_list[2]))
print(today2 ="{}/{}/{}".format(*today_list))

today_list =today.split('/')
c_year = int(today_list[0])+10
today_list[0] = c_year
print(today2 ="{}/{}/{}".format(*today_list))
