import cv2
import imutils
import numpy as np
import argparse
from imutils import paths
from imutils.object_detection import non_max_suppression 

def detect(imagepath):
    frame = cv2.imread(imagepath)

    if frame.shape[1] < 400: # if image width < 400
        (height, width) = frame.shape[:2]
        ratio = width / float(width) # find the width to height ratio
        frame = cv2.resize(frame, (400, width*ratio)) # resize the image according to the width to height ratio

    #frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bound_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride = (4,4), padding = (16,16), scale = 1.02)
    person = 1
    for x,y,w,h in bound_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    

    cv2.putText(frame,'Status : Detecting ', (40,40),cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame,'Source : IMAGE' , (40,70),cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons :{person-1}',(40,100), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)

    #bound_box_cordinates = np.array([[x, y, x + w, y + h] for (x, y, w, h) in bound_box_cordinates])
    #result  = non_max_suppression(bound_box_cordinates, probs=None, overlapThresh=0.65)
    
    #for (xA, yA, xB, yB) in result:
    #    cv2.rectangle(result, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow('OUTPUT : CROWD COUNTING',frame)
    return frame

def detector(frame):
    ap = argparse.ArgumentParser()
    ap.add_argument("-w", "--win-stride", type=str, default="(8, 8)",
	    help="window stride")
    ap.add_argument("-p", "--padding", type=str, default="(16, 16)",
	    help="object padding")
    ap.add_argument("-s", "--scale", type=float, default=1.05,
	    help="image pyramid scale")
    ap.add_argument("-m", "--mean-shift", type=int, default=-1,
	    help="whether or not mean shift grouping should be used")
    args = vars(ap.parse_args())
    winStride = eval(args["win_stride"])
    padding = eval(args["padding"])
    meanShift = True if args["mean_shift"] > 0 else False

    #detect people in the images
    (rects, weights) = HOGCV.detectMultiScale(frame, winStride=winStride,padding=padding,scale=args["scale"], useMeanshiftGrouping=meanShift)

    person = 1
    for x,y,w,h in rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    cv2.putText(frame,'Status : Detecting ', (40,40),cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame,'Source : [~LIVE] ' , (40,70),cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons :{person-1}',(40,100), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)

    #for (x,y,w,h) in rects:
     #   cv2.rectangle(clone, (x,y),(x+w,y+h),(0,0,255),2)

    # Applies non-max supression from imutils package to kick-off overlapped
    # boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    for (xA, yA, xB, yB) in result:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow('OUTPUT : CROWD COUNTING',frame)

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())