import picamera
import time

path = '/home/pi/src4/06_multimedia'
now_str = time.strftime('%Y%m%d_%H%M%S')
camera = picamera.PiCamera()

try:
    while True :
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)
            val = input('photo : 1, video : 2, exit : 9 > ')

            if val == '1':
                camera.capture('%s/photo_%s.jpg' % (path ,now_str))
            elif val == '2':
                camera.start_recording('%s/ video_%s.h264' % (path, now_str))
                time.sleep(1)
                camera.stop_recording()
            elif val == '9':
                break
            else:
                print('잘못된 입력')
finally:
    camera.stop_preview()
