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
        cl=cl-0.1
        if cl<0:
            cl=0
        if cl>1:
            cl=1
        r=1-cl
        g=cl
        if rs!=r or gs!=g or bs!=b:
            mk.led_control(255, r, g, b)
            rs, gs, bs=r, g, b
        time.sleep(0.2)
finally:
    mk.led_control(255, 0, 0, 0)