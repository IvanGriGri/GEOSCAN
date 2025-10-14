from pioneer_sdk import *
import time

mk=Pioneer()
mk.arm()
time.sleep(5)
mk.disarm()