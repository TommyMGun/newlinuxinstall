#!/usr/bin/python3
import os
import time
import re
from sys import exit

def measure_temp():
	'''Gets cpu temperature and converts string to raw digits with regex'''
	tempc = os.popen('vcgencmd measure_temp').read()
	nums = re.findall(r'\d*\d*\d*\.\d*\d*', tempc)
	tempc = float(''.join(nums))
	tempf = tempc*1.8+32
	print('{:.4} Freedom Units\n'.format(tempf))
try:
	while True:
		measure_temp()
		time.sleep(1)
except ValueError:
	print("Value returned from \"vcgencmd measure_temp\" was not a number")
	exit
	
