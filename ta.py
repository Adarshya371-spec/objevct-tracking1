import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

#load the tracker
tracker = cv2.TrackerCSRT_create()

#Read the first fvrame of the video
returned,img = video.read()

#select the bounding box on the image
bbox = cv2.selectROI("TRACKING",img,False)

#initialize the tracker on the image and the bounding box
tracker.init(img,bbox)
print(bbox)

while True:
    check,img = video.read()   

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()
