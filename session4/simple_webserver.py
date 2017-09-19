######################################################################
#       Simple_Webserver.py
#
# This snippet code demonstrate a simple web application
# that run with bottle web sever 
######################################################################

from bottle import route,run,template
from datetime import datetime

@route('/') 
def index():    
    dt = datetime.now()    
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)    
    return template('<b>Pi thinks the date/time is: {{t}}</b>',t=time)

run(host='192.168.43.189', port=90) 
