from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2
import numpy as np
from matplotlib import pyplot as plt
#camera = cv2.VideoCapture(0)
(img,_) = get_video()
#_,im = camera.read()
#cv2.imwrite('thing.png',camera)
#img = cv2.imread(camera,0)


# thresholding
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','ADAPTIVE_THRESH_GAUSSIAN_C']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh6]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
# 2d convolution
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()