from gettext import install
from roku import Roku
from datetime import datetime
from Timer import intervalTimer
import time

hellenZaas = '192.168.0.14'
roku = Roku(hellenZaas)

for value in roku.commands:
    print(value)

print('\n')

for value in roku.apps:
    print(value)

NewsOn6 = roku[580178]
# NewsOn6.launch()
# time.sleep(20)
# roku.home()

current_date = datetime.now().strftime("%H:%M:%S")
print(current_date)
startTime = '06:00:00'
offTime = '09:00:00'

# roku.home()
while True:
    currentTime = datetime.now()
    dayOfWeek = currentTime.strftime("%a")
    intradayTime = currentTime.strftime("%H:%M:%S")

    if dayOfWeek != 'Sat' or dayOfWeek != "Sun" and current_date > startTime and current_date > offTime:
        print(True)
        print(dayOfWeek)
        # NewsOn6.launch()
        # time.sleep(10800)
        # roku.home()
        # time.sleep(20)
        # roku.poweroff()

    else:
        print(False)

    intervalTimer(1)