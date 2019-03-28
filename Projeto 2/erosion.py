#Bruno Sampaio RA: 140004
#Mauricio Luis de Lorenzi RA: 141269

import cv2
import numpy
import pprint

DATA = numpy.array(
    [ 
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0] 
    ], dtype = numpy.uint8 )

kernel = numpy.ones((3,3), numpy.uint8)

erode  = cv2.erode(DATA, kernel, iterations=2)

erode[0,:] = erode[:,0] = erode[:,-1] =  erode[-1,:] = 0

pprint.pprint(DATA)
print("\n")
pprint.pprint(erode)