import time,os

MaxTemp=37.0
EventName='hot_cpu'
BaseUrl='https://maker.ifttt.com/trigger/{}/with/key/{}'
Key='cxotxZpzCKtUnd3m7tkIk4'

def send_notification(temp):
    Json = "'" + '{"value1" : "' + str(temp) + '"}' + "'"
    CompleteUrl = BaseUrl.format(EventName, Key)
    print(CompleteUrl)
    cmd = 'curl --socks5-hostname localhost:9050 -H "Content-Type: application/json" -X POST -d ' + Json + ' ' + CompleteUrl
    os.popen(cmd)

def cpu_temp():
    dev=os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp=dev.read()[5:-3]
    return float(cpu_temp)

while True:
    Temp=cpu_temp()
    print("CPU Temp(c) : " + str(Temp))
    if Temp>MaxTemp:
        print("CPU TOO Hot!")
        send_notification(Temp)
        print("No more notification for : 5")
        time.sleep(5)
