import time
from datetime import datetime, UTC
import pytz

row1 = '2024-11-30 17:55:59'  # UTC
row2 = '24-17-03T5:55:30.255 PM'  # UTC
row3 = '28-02-24 8:55:29.255 -0200'  # TZ = -2 hours


#print(f'current time: {datetime.now()}') # current time
#row1_transformed = datetime.fromisoformat(row1)
#
# row1_transformed = datetime.strptime(row1, '%Y-%m-%d %H:%M:%S')  # strptime перезаписує строку row1 в інстанс class datatime (обєкт)
# print(type(row1_transformed))
# print(row1_transformed)
#
#
# print(type(datetime.strftime(row1_transformed, '%Y-%m-%d %H:%M:%S')))
# print('row1_transformed:', datetime.strftime(row1_transformed, '%Y-%m-%d %H:%M:%S'))  # strftime перезаписує інстанс class datatime (обєкт) в строку row1
# print('row1_transformed:', datetime.strftime(row1_transformed, '%H:%M:%S'))  # можна вивести тільки time
#
# row2_transformed = datetime.strptime(row2, '%y-%d-%mT%H:%M:%S.%f %p')
# print('row2_transformed:', row2_transformed)
#
row3_transformed = datetime.strptime(row3, '%d-%m-%y %H:%M:%S.%f %z')  #приймає строкуб поверне class datetime
# print('row3_transformed:', row3_transformed)
# print(row3_transformed.tzname())


print(type(row3_transformed))
print(row3_transformed.utcoffset())


row4 = '28-02-24 8:55:29.255 -0200'  # TZ = -2 hours

# print(datetime.now(UTC))  # UTC timezone
#
# current_time = datetime.now()
# cur_time_with_tz = time.localtime()
# print(cur_time_with_tz.tm_zone)
# print(current_time)


