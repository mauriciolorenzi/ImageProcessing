import cv2
import os

imagesPath = "images"
images = []

for file in os.listdir(imagesPath): 
    images.append(os.path.join(imagesPath, file))

print(images)

""" img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Img', img)
cv2.imwrite('lena_graysclae.jpg', img)

cv2.waitKey()
cv2.destroyAllWindows() 

----------------

import numpy as np
import cv2

i = cv2.imread('image.jpg')
img = np.array(i, dtype=np.float)
img /= 255.0
cv2.imshow('img',img)
cv2.waitKey(0)

#pre-multiplication
a_channel = np.ones(img.shape, dtype=np.float)/2.0
image = img*a_channel

cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
