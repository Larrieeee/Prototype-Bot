import time

start = round(time.time())
while True:
    time.sleep(1)
    end = round(time.time())

    print(end - start)