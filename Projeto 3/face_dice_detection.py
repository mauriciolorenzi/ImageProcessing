import cv2
import numpy

KERNEL = numpy.ones((10,10),numpy.uint8)

dices = cv2.imread('dados.jpg', cv2.IMREAD_COLOR)

dices_bgr = dices.copy()

dices_yuv = cv2.cvtColor(dices_bgr, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
dices_yuv[:,:,0] = cv2.equalizeHist(dices_yuv[:,:,0])

# convert the YUV image back to RGB format
dices_bgr = cv2.cvtColor(dices_yuv, cv2.COLOR_YUV2BGR)

dices_bgr = cv2.cvtColor(dices_bgr, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(dices_bgr, 127, 255, cv2.THRESH_BINARY_INV)

thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, KERNEL)

#dices = cv2.bitwise_not(dices)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

height, width = dices_bgr.shape
min_x, min_y  = width, height
max_x = max_y = 0

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(dices)

# computes the bounding box for the contour, and draws it on the frame,
for contour in contours :
"""    (x,y,w,h) = cv2.boundingRect(contour)
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    cv2.rectangle(dices, (x,y), (x+w,y+h), (0,0,255), 1)"""
    for marker in keypoints:
        #center
"""        x,y = numpy.int(marker.pt[0]),numpy.int(marker.pt[1])
        pos = numpy.int(marker.size / 2)
        cv2.circle(dices,(x,y),3,255,-1)
        cv2.rectangle(dices,(x-pos,y-pos),(x+pos,y+pos),0,1)"""

    
cv2.imshow("Blobs = "+ str(len(keypoints)), dices)
cv2.waitKey()
cv2.destroyAllWindows()