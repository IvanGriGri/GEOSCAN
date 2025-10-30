from pioneer_sdk import *
import time

mk=Pioneer()
try:
    mk.arm()
    mk.takeoff()
    input()
finally:
    mk.land()
