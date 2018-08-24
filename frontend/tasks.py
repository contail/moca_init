from web.celery import app

import subprocess
@app.task
def run_web_server(ip_address, port):
    print (ip_address)
    print (port)
    command = 'python manage.py runserver {0}:{1}'.format(ip_address,port)
    pid  = subprocess.Popen(command,  stdout=subprocess.PIPE, shell=True)

    print (pid)


