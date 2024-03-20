from datetime import datetime
import time

now = datetime.now()
# start_time = datetime.date(now.year,now.month,now.day, now.hour, now.minute, now.second)
# print(start_time)

end_time = datetime(2024,6,24)


# print(d_day.days)
print(end_time)
print((end_time - now).days)   # days: 날짜만 출력
print(end_time - now) # 날짜, 시간까지 출력