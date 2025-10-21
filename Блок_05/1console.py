from pioneer_sdk import *
import time

mk=Pioneer()
while True:
    print(mk.get_dist_sensor_data())
    time.sleep(0.1)