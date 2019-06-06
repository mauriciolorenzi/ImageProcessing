#Douglas Barioni Amorim   RA: 130081
#Mauricio Luis de Lorenzi RA: 141269

import cv2
import matplotlib.pyplot as plt
import numpy

CHROMA_KEY_VIDEO = cv2.VideoCapture('chroma_key_video.mp4')
BACKGROUND_VIDEO = cv2.VideoCapture('background_video.mp4')

while CHROMA_KEY_VIDEO.isOpened() and BACKGROUND_VIDEO.isOpened():        
        ret, frame = CHROMA_KEY_VIDEO.read()
        ret_background, frame_background = BACKGROUND_VIDEO.read()

        if(ret and ret_background) : 
                copy_frame = numpy.copy(frame)
                copy_frame = cv2.cvtColor(copy_frame, cv2.COLOR_BGR2RGB)
                frame_background = cv2.cvtColor(frame_background, cv2.COLOR_BGR2RGB)

                lower_green = numpy.array([0, 100, 0])    
                upper_green = numpy.array([100, 255, 70])

                mask = cv2.inRange(copy_frame, lower_green, upper_green)

                masked_frame = numpy.copy(copy_frame)
                masked_frame[mask != 0] = [0, 0, 0]

                # Crop the image
                crop_background = frame_background[0:720, 0:1280]

                # Mask the cropped background
                crop_background[mask == 0] = [0, 0, 0]

                # Add the two images together to create a complete image
                final_image = cv2.cvtColor(crop_background + masked_frame, cv2.COLOR_RGB2BGR)

                # Show the result
                cv2.imshow('chroma key video', final_image)                

        if cv2.waitKey(25) & 0xFF == ord('q'):
                break

CHROMA_KEY_VIDEO.release()
BACKGROUND_VIDEO.release()
cv2.waitKey()
cv2.destroyAllWindows()