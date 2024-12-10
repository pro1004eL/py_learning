import time


if __name__ == '__main__':

    ct = time.localtime()

    print(ct)

    print(f'current time: {ct.tm_hour}:{ct.tm_min}')

    cur_time_sec = time.time()
    time.sleep(1.5)
    print(f'Diff was {time.time() - cur_time_sec}')

    while time.time() - cur_time_sec < 5: # поки не пройде 5 секунд
        print('Waiting...')
        time.sleep(0.8)







