from pioneer_sdk import *
import random

mk=Pioneer()
try:
    while True:
        input()
        mk.led_control(255, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100)
finally:
    mk.led_control(255, 0, 0, 0)