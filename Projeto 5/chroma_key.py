#
#Mauricio Luis de Lorenzi RA: 141269

import cv2
import numpy

CHROMA_KEY_VIDEO = cv2.VideoCapture('chroma_key_video.mp4')
BACKGROUND_VIDEO = cv2.VideoCapture('chroma_key_video.mp4')
MOG = cv2.createBackgroundSubtractorMOG2()
KERNEL = numpy.ones((11, 11), numpy.uint8)

while CHROMA_KEY_VIDEO.isOpened() and BACKGROUND_VIDEO.isOpened():        
        ret, frame = CHROMA_KEY_VIDEO.read()
        ret_backgorund, frame_background = BACKGROUND_VIDEO.read()

        if(ret and ret_backgorund) : 
                frame2 = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
                mask = MOG.apply(frame2)

                gaussianBlur = cv2.GaussianBlur(mask, (11, 11), 3.5)
                ret,thresh = cv2.threshold(gaussianBlur, 10, 255, cv2.THRESH_BINARY)
                cv2.imshow("Real", frame)

                #Remove the background        
                im = frame2 - thresh

                cv2.imshow("chroma key video", cv2.cvtColor(im, cv2.COLOR_GRAY2BGR))

        if cv2.waitKey(25) & 0xFF == ord('q'):
                break

CHROMA_KEY_VIDEO.release()
BACKGROUND_VIDEO.release()
cv2.waitKey()
cv2.destroyAllWindows()