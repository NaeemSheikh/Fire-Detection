import io
import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, format='jpeg'):
        #Truncate the stream to the current position (in case
        # prior iterations output a longer image)
        stream.truncate()
        stream.seek(0)
        for line in stream:
            print line
        #img = cv2.imread(stream, cv2.IMREAD_COLOR)
        #cv2.imshow('i',img)
        
		
