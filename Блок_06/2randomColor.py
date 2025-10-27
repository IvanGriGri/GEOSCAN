from pioneer_sdk import *
import random

mk=Pioneer()
while True:
    input()
    mk.led_control(255, random.randint(0, 100)/100, random.randint(0, 100)/100, random.randint(0, 100)/100)