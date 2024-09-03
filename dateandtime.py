from datetime import date, datetime, time, timezone

print(' ')

d = date.today()
n = datetime.now()
m = n.minute
h = n.hour
print(f'{d}, {h}:{m}')

