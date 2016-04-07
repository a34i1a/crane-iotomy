import cv2
import time
import usb.core
import usb.util
import sys
import time
from depthmap import *
#from freenect import sync_get_depth as get_depth, sync_get_video as get_video
#filename = 'hi.avi'
#fps = 16

# 
# cap = get_video

#in this way it always works, because your get the right "size"
#size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
#         int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#fourcc = cv2.cv.FOURCC('8', 'B', 'P', 'S')     #works, large
#out = cv2.VideoWriter(filename, fourcc, fps, size, True)

#in this way, you must set the "size" to your size, 
#because you don't know the default "size" is right or not
#cap.set(3, 640)
#cap.set(4, 480)
#out = cv2.VideoWriter(filename, fourcc, fps, (640, 480), True)

while(1):
#     ret, frame = cap.read()
	#(camera,_) = get_video()
	depth = getDepthMap()
    #if ret == True:
	#out.write(camera)
	cv2.imshow('frame', depth)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break;
	else:
		print 'Error...'


# cap.release()
out.release()
cv2.destroyAllWindows()