######################################################################
#	EmailIfttt.py
#
# This program measure Raspberry pi cpu temprature and then send  
# to ifttt server with make http request.
######################################################################

import time,os

MaxTemp = 37.0
EventName = 'cpu_hot'
BaseUrl = 'https://maker.ifttt.com/trigger/{}/with/key/{}'
Key = 'cxotxZpzCKtUnd3m7tkIk4'

def SendNotification(temp):
    json = "'" + '{"value1" : "' + str(temp) + '"}' + "'"
    completeUrl = BaseUrl.format(EventName, Key)
    cmd = 'curl --socks5-hostname localhost:9050 -H "Content-Type: application/json" -X POST -d {} {}'.format(json, completeUrl)
    os.popen(cmd)

def CpuTemp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    temp = dev.read()[5:-3]
    return float(temp)

while True:
    temp = CpuTemp()
    print("CPU Temp(c) : {}".format(temp))
    if temp > MaxTemp:
        print("CPU TOO Hot!")
        SendNotification(temp)
        print("No more notification for : 5")
        time.sleep(5)
