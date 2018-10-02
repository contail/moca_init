
import picamera         #picamera를 불러온다.
from time import sleep  #중간에 5초 딜레이를 위한 sleep 함수

camera = picamera.PiCamera()         #picamera 생성
camera.resolution = (640, 480)
camera.framerate = 35
camera.start_preview()
camera.start_recording('test.h264') #녹화 시작
sleep(10)                             #5초간 대기
camera.stop_recording()
camera.stop_preview()
