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

#----- State on and off time logic -----
startTime = '06:00:00'
offTime = '09:00:00'

#----- Print Current Intraday Date -----
current_date = datetime.now().strftime("%H:%M:%S")
print(current_date)

#----- Run Loop -----
while True:
    currentTime = datetime.now()
    current_date = datetime.now().strftime("%H:%M:%S")
    dayOfWeek = currentTime.strftime("%a")

    print("\n")
    print("===================================")
    print(f"Day of the Week: {dayOfWeek}")
    print(f"Intra Day Date: {current_date}")
    print(f"Start Time: {startTime}")
    print(f"End Time: {offTime}")

    if dayOfWeek != 'Sat' and dayOfWeek != "Sun" and current_date > startTime and current_date < offTime:
        print("Activate Roku: True")
        roku.poweron()
        NewsOn6.launch()
        time.sleep(10800)
        roku.home()
        time.sleep(20)
        roku.poweroff()

    else:
        print("Activate Roku: False")

    intervalTimer(5)