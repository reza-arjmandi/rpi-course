from bottle import route,run,template
from datetime import datetime


@route('/') 
def index():    
    dt = datetime.now()    
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)    
    return template('<b>Pi thinks the date/time is: {{t}}</b>',t=time)

run(host='192.168.43.189', port=90) 
