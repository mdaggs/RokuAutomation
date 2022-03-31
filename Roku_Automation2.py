from roku import Roku
from datetime import datetime
from Timer import intervalTimer
import time
from config import *

#----- Define Your Roku Instance -----
roku = Roku(livingRoom)

#----- Print Available Commands -----
for value in roku.commands:
    print(value)

print('\n')

#----- Print Apps on Your Roku Device -----
for value in roku.apps:
    print(value)

#----- State Your App instances -----
NewsOn6 = roku[580178]

#----- Print Current Intraday Date -----
current_date = datetime.now().strftime("%H:%M:%S")
print(current_date)

#----- Run -----
currentTime = datetime.now()
current_date = datetime.now().strftime("%H:%M:%S")
dayOfWeek = currentTime.strftime("%a")

print("\n")
print("===================================")
# print(f"Day of the Week: {dayOfWeek}")
# print(f"Intra Day Date: {current_date}")

print("Activate Roku: True")
print(f"Turning on {livingRoom} Roku")
roku.poweron()
time.sleep(60)
print("Launching News on 6")
NewsOn6.launch()
time.sleep(10800)
roku.home()
print("Preparing to Turn off..")
time.sleep(60)
roku.poweroff()
