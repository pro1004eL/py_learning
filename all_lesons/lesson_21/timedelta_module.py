import time
from datetime import datetime, UTC, timedelta

import pytz

client_time = '2024-12-02 18:09:10.226311'
server_time = '2024-12-02 18:09:10.226311+00:00'


client_time_dt = datetime.strptime(client_time, '%Y-%m-%d %H:%M:%S.%f') # зі строки client_time зробили обєкт datatime
server_time_dt = datetime.strptime(server_time, '%Y-%m-%d %H:%M:%S.%f%z')

local_tz = time.localtime().tm_zone  # поточна тайм зона (для Київа = EET)
client_time_dt2 = pytz.timezone(local_tz).localize((client_time_dt))  # додали локальну тайм зону клієнта для обэкта datatime EET == Europe/Kyiv (+02:00)

print(local_tz)

print(client_time_dt)
print(server_time_dt)

diff_between_times = server_time_dt - client_time_dt2

print(type(diff_between_times))
print(f'difference between server and client timezone= {diff_between_times.seconds} seconds')


# row3 = '28-02-24 8:55:29.255 -0200'  # TZ = -2 hours
#
# row3_transformed = datetime.strptime(row3, '%d-%m-%y %H:%M:%S.%f %z')  #приймає строкуб поверне class datetime
#
# cur_time = datetime.now(UTC)
#
# print(cur_time)
# print(row3_transformed)
#
# print(cur_time - row3_transformed)