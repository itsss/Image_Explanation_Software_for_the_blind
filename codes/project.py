import RPi.GPIO as GPIO
import time
import os
import picamera

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed, Execute Explain Images For the Blind Software.')
        camera = picamera.PiCamera()
        camera.capture('/home/eifb/caption-master/images/piimage.jpg')
        os.system('python generate_caption.py -i ../images/piimage.jpg')
        time.sleep(0.2)
        quit()
