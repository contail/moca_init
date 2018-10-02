from web.celery import app

import subprocess
@app.task
def run_web_server(ip_address, port):

    command = 'python manage.py runserver {0}:{1}'.format(ip_address,port)
    subprocess.Popen(command,  stdout=subprocess.PIPE, shell=True)


@app.task
def stop_web_server(ip_address, port):
    command = "kill -9 $(ps | grep {0}:{1}".format(ip_address, port)
    append_command = "| awk '{ print $1 }')"
    subprocess.Popen(command+append_command, stdout=subprocess.PIPE, shell=True)

@app.task
def start_piCamera():
    command = "python recode.py"
    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

@app.task
def change_mp4File():
    command = "MP4Box -fps 30 -add test.h264 test1.mp4"
    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)


