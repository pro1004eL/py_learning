from datetime import datetime, timedelta



today = datetime.now()
print(today)

seven_days_ago = today - timedelta(seconds=7*24*60*60)  # 7 days in seconds

print(seven_days_ago)


def is_diff_more_30_sec(time_A:datetime, time_B:datetime):
      time_difference = time_B - time_A  # Обчислення різниці у часі

      return time_difference > timedelta(seconds=31) # поверне True, якщо різниця більше 31 секунди

# Перевірка роботи
time_a = datetime.now()  # отримаємо поточний час
time_b = time_a + timedelta(seconds=32) # штучно збільшимо його на 32 секунди
if is_diff_more_30_sec(time_a, time_b):
   print("WARNING! Різниця більше 31 секунд!")