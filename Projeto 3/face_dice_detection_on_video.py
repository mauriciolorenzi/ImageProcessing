#Mauricio Luis de Lorenzi RA: 141269

import cv2
import numpy

KERNEL = numpy.ones((7, 7),numpy.uint8)
DICE_KERNEL = numpy.ones((5, 5),numpy.uint8)
FACE_BALLS_NUMBERS = []
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SIZE = 1
FONT_COLOR = (0, 0, 255)
FONT_SCALE = 2
LINE_TYPE = cv2.LINE_AA
DICES_VIDEO = cv2.VideoCapture('dice_video.mp4')
COUNT = 0
MIN_RANGE = 2200
MAX_RANGE = 4000

def DetectDiceFaceNumber(dices):
        FACE_BALLS_NUMBERS = []
        FACE_BALLS_NUMBER = 0
        numbersX = []
        numbersY = []
        
        # Copy the image
        dices_bgr = dices.copy()

        # Convert the BGR dices image to GRAY format
        dices_gray = cv2.cvtColor(dices_bgr, cv2.COLOR_BGR2GRAY)

        # Do the binarization of the gray format image
        _,thresh = cv2.threshold(dices_gray, 127, 255, cv2.THRESH_BINARY)
        #_,thresh = cv2.threshold(dices_bgr, 127, 0, cv2.THRESH_BINARY_INV)

        # Apply Opening morphological transformation (erosion followed by dilation) to remove all noises of the image
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, KERNEL)
        #thresh = cv2.dilate(thresh, numpy.ones((5, 5), numpy.uint8), KERNEL)
        cv2.imshow("thresh", thresh)
      
        # Find the contours (dices' faces)
        contours,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Set up the detector with default parameters
        detector = cv2.SimpleBlobDetector_create()

        # Computes the bounding box for the contour
        for contour in contours :
                # Get the respective x and y of start and end point
                (x,y,w,h) = cv2.boundingRect(contour)
                # Get only the dice's face image
                roi = dices[y : y + h, x : x + w].copy()

                # Get the roi area size
                roi_area = w * h

                if roi_area > MIN_RANGE and roi_area < MAX_RANGE:
                        # Getting the roi in grayscale
                        #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                        # Do the binarization of the grayscale roi
                       # _, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)
                        #roi = cv2.morphologyEx(roi, cv2.MORPH_OPEN, DICE_KERNEL)
                        # Get the keypoints
                        keypoints = detector.detect(roi)
                        if len(keypoints) > 0:
                                cv2.imshow("roi", roi)
                                # X start position of the number
                                #numberX = int(x + (w / 2))
                                numbersX.append(int(x + (w / 2)))

                                # Y start position of the number
                                #numberY = int(y + (h / 2))
                                numbersY.append(int(y + (h / 2)))

                                # Count the number of face's balls
                                for marker in keypoints:
                                        # Increment the number of balls found in dices' face                                
                                        FACE_BALLS_NUMBER += 1

                                # Append the dice's face balls number to an array
                                if FACE_BALLS_NUMBER != 0:
                                        FACE_BALLS_NUMBERS.append(FACE_BALLS_NUMBER)

                                # Restart the count of a face's number 
                                FACE_BALLS_NUMBER = 0  
                                #cv2.rectangle(dices, (x,y), (x+w,y+h), (0,0,255), 2)
                        else:
                                cv2.destroyWindow("roi")             
        
        return FACE_BALLS_NUMBERS, numbersX, numbersY

while DICES_VIDEO.isOpened() :        
        ret, frame = DICES_VIDEO.read()
        #COUNT += 1

        #if COUNT == 10:
        #        COUNT = 0
        FACE_BALLS_NUMBERS, numbersX, numbersY = DetectDiceFaceNumber(frame)
        # Print the number of balls on the right face]
        if len(FACE_BALLS_NUMBERS) > 0:
                for i in range(len(FACE_BALLS_NUMBERS)):
                        cv2.putText(frame, str(FACE_BALLS_NUMBERS[i]), (numbersX[i], numbersY[i]) , FONT, FONT_SIZE, FONT_COLOR, FONT_SCALE, LINE_TYPE)

        cv2.imshow("dices with numbered faces", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
                break

cv2.waitKey()
cv2.destroyAllWindows()