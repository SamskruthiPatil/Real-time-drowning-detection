import cv2
import os
import time
#import pafy


step = 10
frames_count = 3
cam = cv2.VideoCapture('countfinal.mp4')
ret, frame = cam.read()
print(ret)
if ret:
    print(6)
    name = './data/frame1.jpg'
# writing the extracted images
cv2.imwrite(name, frame)
cam.release()
cv2.destroyAllWindows()