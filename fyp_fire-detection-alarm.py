import cv2
import numpy as np
from firebase import firebase
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

def LED_alert(st):
    ct = time.time()
    if ct < (st + 10):
        GPIO.output(7,True)
        time.sleep(0.25)
    else:
        GPIO.output(7,False)
        time.sleep(0.25)

#init GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11,  GPIO.OUT)

#init picamera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)
#fgbg = cv2.BackgroundSubtractorMOG2(history=1, varThreshold=16, bShadowDetection=True)

#init firebase App
applink = '[ PLACEHOLDER ]' # Insert url for the app here
firebase = firebase.FirebaseApplication(applink, None)

isFire = False
threshold = 400
start = None
font = cv2.FONT_HERSHEY_SIMPLEX


#fire detection
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = np.array(image, dtype=np.uint8)
    blur = cv2.GaussianBlur(image, (21,21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    #fgmask = fgbg.apply(image)
    lower = np.array([1,30,169], dtype = "uint8")
    upper = np.array([36,255,255], dtype = "uint8")
    mask1 = cv2.inRange(hsv,lower,upper)
    
    lower = np.array([30,0,245], dtype = "uint8")
    upper = np.array([180,8,255], dtype = "uint8")
    mask2 = cv2.inRange(hsv,lower,upper)
    fmask = cv2.bitwise_or(mask1,mask2)
    firecount = cv2.countNonZero(fmask)
    output = cv2.bitwise_and(image, image, mask = fmask)
    if isFire:
        cv2.putText(image, "Fire detected!", (10, 230), font, 0.5, (0,0,255), 1)
    
    cv2.imshow("Fire detector", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    
    if key == ord("q"):
            break
    
    wasFire = isFire
    isFire = firecount > threshold
    
    if isFire:
        start = time.time()
        GPIO.output(11, True)
        time.sleep(0.001)
        GPIO.output(11, False)
        time.sleep(0.001)
    
    if start == None: continue
    LED_alert(start)    
    
    if wasFire != isFire:
        firebase.put('fire-state', 'isFire', isFire)
    

cv2.destroyAllWindows()
GPIO.cleanup()
