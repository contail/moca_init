import picamera         #picamera를 불러온다.
from time import sleep  #중간에 5초 딜레이를 위한 sleep 함수

camera = picamera.PiCamera()         #picamera 생성
camera.start_recording('test.h264') #녹화 시작
sleep(5)                             #5초간 대기
camera.stop_recording()