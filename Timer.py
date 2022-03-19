from datetime import datetime
import time
import numpy as np

def intervalTimer(interval):
#----------------------Wait Till next Candle----------------------

	def sleepTimeSeconds(time_1, time_2):
		# return round(int(time_2.second - time_1.second))
		return round(int(time_2.second - time_1.second))

		#---Calculate Minute Replacer---
	def sleepTimeMinutes(interval, timeMinute):

		if interval == 1:
			time.sleep(1)
			return timeMinute

		if interval == 5:
			round_list = [4, 9, 14, 19, 24, 30, 34, 39, 44, 49, 54, 59]
			x = []
			for value in round_list:
				if value > timeMinute:
					x.append(value)
					break
				else:
					pass

			return x[0]

		elif interval == 10:
			round_list = [9, 19, 29, 39, 49, 59]
			x = []
			for value in round_list:
				if value > timeMinute:
					x.append(value)
					break
				else:
					pass

			return x[0]

		elif interval == 30:
			round_list = [29, 59]
			x = []
			for value in round_list:
				if value > timeMinute:
					x.append(value)
					break
				else:
					pass

			return x[0]

		elif interval == 60:
			round_list = [59]
			x = []
			for value in round_list:
				if value > timeMinute:
					x.append(value)
					break
				else:
					pass

			return x[0]
		else:
			pass
#----------------------------------------------------------------------
	
	#Grab Current Time and a TimeDelta Varaible
	time_1 = datetime.now()
	time_2 = datetime.now().replace(second=59)

	#Grab Seconds to next minute and then Minutes to sleep
	futureSecond = sleepTimeSeconds(time_1, time_2)
	futureMinute = sleepTimeMinutes(interval, time_1.minute)

	#Print Variables
	# print(time_1)
	#Replace current minute with a future minute
	finalTime = time_2.replace(minute=futureMinute)
	# print(finalTime)

	#Find Total Sleep Duration
	sleepDuration = finalTime - time_1

	print('\n')
	print("Current Time: %s" % time_1)
	print("Time Till the Next interval: %s" % (sleepDuration))
	print("Seconds Time Till the Next inteverval: %s" % (sleepDuration.seconds))

	time.sleep(sleepDuration.seconds)
	print('\n')

