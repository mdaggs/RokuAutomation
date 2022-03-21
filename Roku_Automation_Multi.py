from roku import Roku
from datetime import datetime
from Timer import intervalTimer
import time
from config import *

#----- Run Loop -----
while True:
    #----- State on and off time logic -----
    startTime = '06:00:00'
    offTime = '09:00:00'
    startTime = '19:43:00'
    offTime = '19:50:00'

    #----- Print Current Intraday Date -----
    currentTime = datetime.now()
    current_date = datetime.now().strftime("%H:%M:%S")
    dayOfWeek = currentTime.strftime("%a")

    print("\n")
    print("===================================")
    print(f"Day of the Week: {dayOfWeek}")
    print(f"Intra Day Date: {current_date}")
    print(f"Start Time: {startTime}")
    print(f"End Time: {offTime}")

    # if dayOfWeek != 'Sat' and dayOfWeek != "Sun" and current_date > startTime and current_date < offTime:
    if current_date > startTime and current_date < offTime:

        #----- Activate Roku -----
        for ipAddress in ipList:

            #----- Define Your Roku Instance -----
            roku = Roku(ipAddress)
            time.sleep(5)

            #----- State Your App instances -----
            NewsOn6 = roku[580178]

            #----- Print Roku Info -----
            print("Activate Roku: True")
            print(f"IP: {ipAddress}")
            print(f"Roku: {roku}")
            print("-----")

            #----- Command Roku -----
            # roku.poweron()
            time.sleep(5)
            # NewsOn6.launch()

        #----- Sleep Until Next Step -----
        # time.sleep(10800)

        #----- Turn Of Roku -----
        for ipAddress in ipList:

            #----- Define Your Roku Instance -----
            roku = Roku(ipAddress)
            time.sleep(5)
            print(f"Roku in Off Part")

            #----- Command Roku -----
            # roku.home()
            time.sleep(10)
            # roku.poweroff()

    else:
        print("Activate Roku: False")

    intervalTimer(1)