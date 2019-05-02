#Mauricio Luis de Lorenzi RA: 141269

import cv2
import numpy

KERNEL = numpy.ones((10,10),numpy.uint8)
FACE_BALLS_NUMBER = 0
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SIZE = 1
FONT_COLOR = (0, 0, 255)
FONT_SCALE = 2
LINE_TYPE = cv2.LINE_AA
DICES_VIDEO = cv2.VideoCapture('dice_video.mp4')
COUNT = 0

def DetectDiceFaceNumber(dices):
        FACE_BALLS_NUMBER = 0
        numberX = 0
        numberY = 0

        # Get the dices image
        #dices = cv2.imread('dados.jpg', cv2.IMREAD_COLOR)

        # Copy the image
        dices_bgr = dices.copy()

        # Convert the BGR dices image to YUV format
        dices_yuv = cv2.cvtColor(dices_bgr, cv2.COLOR_BGR2YUV)

        # Equalize the histogram of the Y channel
        dices_yuv[:,:,0] = cv2.equalizeHist(dices_yuv[:,:,0])

        # Convert the YUV dices image back to BGR format
        dices_bgr = cv2.cvtColor(dices_yuv, cv2.COLOR_YUV2BGR)

        # Convert the BGR dices image to GRAY format
        dices_gray = cv2.cvtColor(dices_bgr, cv2.COLOR_BGR2GRAY)

        # Do the binary inversion of the gray format image
        _,thresh = cv2.threshold(dices_gray, 127, 255, cv2.THRESH_BINARY_INV)

        # Apply Opening morphological transformation (erosion followed by dilation) to remove all noises of the image
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, KERNEL)

        # Find the contours (dices' faces)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Set up the detector with default parameters
        detector = cv2.SimpleBlobDetector_create()

        # Computes the bounding box for the contour
        for contour in contours :
                # Get the respective x and y of start and end point
                (x,y,w,h) = cv2.boundingRect(contour)
                
                # Get the only the dice's face image
                roi = dices[y : y + h, x : x + w].copy()

                # Get the keypoints
                keypoints = detector.detect(roi)

                # Count the number of face's balls
                for marker in keypoints:
                        # Increment the number of balls found in dices' face                                
                        FACE_BALLS_NUMBER += 1

                        # X start position of the number
                        numberX = int(x + (w / 2))

                        # Y start position of the number
                        numberY = int(y + (h / 2))

                # Print the number of balls on the right face
                cv2.putText(dices, str(FACE_BALLS_NUMBER), (numberX, numberY) , FONT, FONT_SIZE, FONT_COLOR, FONT_SCALE, LINE_TYPE)
                # Restart the count of a face's number 
                FACE_BALLS_NUMBER = 0
        
        cv2.imshow("dices with numbered faces", dices)

while DICES_VIDEO.isOpened() :        
        ret, frame = DICES_VIDEO.read()
        COUNT += 1

        if COUNT == 15:
                COUNT = 0
                DetectDiceFaceNumber(frame)
        else:
                cv2.imshow("dices with numbered faces", frame) 

        if cv2.waitKey(25) & 0xFF == ord('q'):
                break


cv2.waitKey()
cv2.destroyAllWindows()