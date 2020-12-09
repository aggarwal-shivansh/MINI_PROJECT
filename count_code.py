import cv2
import numpy as np
import detect
from imutils.object_detection import non_max_suppression    
import imutils
import urllib.request


#URL = "http://192.168.43.172:8080"

'''def trial():
    while True:    
        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
        img = cv2.imdecode(img_arr,-1)
        cv2.imshow('IPWebcam',img)
        if cv2.waitKey(1):
            break'''
def Webcam():
    #cap = cv2.VideoCapture('http://192.168.43.172:8080/video')
    cap = cv2.VideoCapture(0)
    #if not cap.isOpened():
    #    raise IOError("Unable to open webcam")

    while True:
        ret,frame = cap.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # apply threshold. all pixels with a level larger than 80 are shown in white. the others are shown in black:
        #ret,frame = cv2.threshold(frame,80,255,cv2.THRESH_BINARY)
        #cv2.imshow('Camera',frame)
        frame = imutils.resize(frame, width=min(1200, frame.shape[1]))
        result = detect.detector(frame.copy())
        #frame = detect.detect(frame.copy())
        if cv2.waitKey(40) == 27:
            break
        
    cap.release()
def localDetect(image_path):
    result = []
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    if len(image) <= 0:
        print("[ERROR] could not read your local image")
        return result
    print("[INFO] Detecting people")
    result = detect.detect(image,'IMAGE')
    #detect.detector(image)

    # shows the result
    #   cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    #cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return (result, image)
 


cv2.destroyAllWindows()
