import time,os,urllib,urllib2
import socket
import socks

MaxTemp=37.0
EventName='hot_cpu'
BaseUrl='https://maker.ifttt.com/trigger/{}/with/key/{}'
Key='cxotxZpzCKtUnd3m7tkIk4'

def send_notification(temp):
    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    #socket.socket = socks.socksocket
    Json=urllib.urlencode({'value1' : str(temp)})
    CompleteUrl=BaseUrl.format(EventName, Key)
    Response=urllib2.urlopen(url=CompleteUrl, data=Json)
    print(Response.read())

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
