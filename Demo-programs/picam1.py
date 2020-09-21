from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

def get_info(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(hsv[y,x])
        cv2.imwrite('test1.jpg', img2)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',get_info)

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

#fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (320,240))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	
	img2 = np.array(image, dtype=np.uint8)
	#out.write(img2)
	blur = cv2.GaussianBlur(img2, (21,21), 0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	
	lower = np.array([0,30,169], dtype = "uint8")
        upper = np.array([36,255,255], dtype = "uint8")
        mask1 = cv2.inRange(hsv,lower,upper)
        
        lower = np.array([30,0,245], dtype = "uint8")
        upper = np.array([180,8,255], dtype = "uint8")
        mask2 = cv2.inRange(hsv,lower,upper)

        fmask = cv2.bitwise_or(mask1,mask2)
        
        output = cv2.bitwise_and(img2, img2, mask = fmask)
        firecount = cv2.countNonZero(fmask)
        print firecount
	cv2.imshow("Frame", output)
	#print hsv[120,160], img2[120,160]
	key = cv2.waitKey(1) & 0xFF

	rawCapture.truncate(0)
	
	if key == ord("q"):
		break
#out.release()
cv2.destroyAllWindows()