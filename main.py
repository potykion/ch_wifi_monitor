import time
from datetime import datetime

from ch_wifi_monitor.db import insert_speed
from ch_wifi_monitor.speed import request_speed, format_speed
from ch_wifi_monitor.utils import to_mbs

HOUR = 60 * 60

if __name__ == '__main__':
    while True:
        print(datetime.now())
        print("Calculating speed...")
        speed = format_speed(request_speed())
        print(f'Download speed: {to_mbs(speed["download_speed"])} Mb/s')
        print("Inserting speed to ClickHouse...")
        insert_speed(speed)
        print("Complete")
        time.sleep(HOUR)
