######################################################################
#	cpu_temp.py
#
# This program measure Raspberry pi cpu temprature and print it 
# every one second
#####################################################################

import os, time

cmd='/opt/vc/bin/vcgencmd measure_temp'

while True:
    dev = os.popen(cmd)
    cpuTempStr = dev.read()[5:-3]
    cpuTemp=float(cpuTempStr)
    print(cpuTemp)
    time.sleep(1)
