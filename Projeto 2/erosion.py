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

COLOR = 127
SQUARES = 0

kernel = numpy.ones((3,3), numpy.uint8)

erode  = cv2.erode(DATA, kernel)

erode[0,:] = erode[:,0] = erode[:,-1] =  erode[-1,:] = 0

pprint.pprint(DATA)

for i in range(len(erode)):
    for j in range(len(erode[0])):
        if erode[i,j] == 1:            
            if (erode[i-1,j] == 1 or erode[i-1,j] == 0) and (erode[i+1,j] == 1 or erode[i+1,j] == 0) and (erode[i,j-1] == 1 or erode[i,j-1] == 0) and (erode[i,j] == 1 or erode[i,j] == 0) and (erode[i-1, j-1] == 1 or erode[i-1,j-1] == 0) and (erode[i+1,j+1] == 1 or erode[i+1,j+1] == 0) and (erode[i+1, j-1] == 1 or erode[i+1,j-1] == 0) and (erode[i+1,j-1] == 1 or erode[i+1,j-1] == 0):
                erode[i,j] = COLOR
                erode[i,j-1] = COLOR
                erode[i,j+1] = COLOR
                erode[i-1,j] = COLOR                
                erode[i+1,j] = COLOR
                erode[i-1, j-1] = COLOR
                erode[i+1, j+1] = COLOR
                erode[i+1, j-1] = COLOR
                erode[i-1, j+1] = COLOR
                COLOR += 1
                SQUARES += 1

print("\n")
pprint.pprint(erode)

print("\n Numero de quadrados: {}".format(SQUARES))