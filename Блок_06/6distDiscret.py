from pioneer_sdk import *
import time

r=0
g=0
b=0
rs=0
bs=0
gs=0

mk=Pioneer()
try:
    while True:
        cl=mk.get_dist_sensor_data()
        if cl==None:
            continue
        if cl<0.5:
            r=1
            g=0
            b=0
        elif cl>0.5 and cl<1:
            r=0
            g=1
            b=0
        elif cl>1:
            r=0
            g=0
            b=1
        if rs!=r or gs!=g or bs!=b:
            mk.led_control(255, r, g, b)
            rs, gs, bs=r, g, b
        time.sleep(0.2)
finally:
    mk.led_control(255, 0, 0, 0)