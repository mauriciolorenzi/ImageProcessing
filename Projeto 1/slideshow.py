#Mauricio Luis de Lorenzi RA: 141269

import cv2
import os
import numpy

IMAGES_PATH = "images"  # Root where the images are
IMAGES = []  # Images path array
SLIDE_QUEUE = []  # The slide images queue
CHANGE_IMAGE = 2000  # 2 seconds to change between images
TRANSITION = 50  # 50 mili seconds of transition  int the addWeighted loop
BORDER_SIZE = 20  # 20px for size of the image border
WATER_MARK_PATH = "water_mark.png"  # Path of the water mark

# Resize the image to 100 x 100
def Resize(image):
    return cv2.resize(image, (400, 300), interpolation=cv2.INTER_AREA)

# Add border 20 px into the image
def AddBorder(image):
    return cv2.copyMakeBorder(image, BORDER_SIZE, BORDER_SIZE, BORDER_SIZE, BORDER_SIZE, cv2.BORDER_CONSTANT, value=[255, 255, 255, 255])

# Add a water mark into the image
def AddWaterMark(image):
    # Loading the water mark  
    waterMarkImage = cv2.imread(WATER_MARK_PATH)

    # This point represent the width point
    xInit = BORDER_SIZE
    xEnd = waterMarkImage.shape[1] + BORDER_SIZE

    # This point represent the height point
    yInit = image.shape[0] - BORDER_SIZE - waterMarkImage.shape[0]
    yEnd = image.shape[0] - BORDER_SIZE

    # Getting a region of interest
    roi = image[yInit:yEnd, xInit:xEnd]
  
    # Adding alpha to the roi and the water mark image
    roi = cv2.addWeighted(roi, 0.5, waterMarkImage, 0.5, 0)
    
    # Putting the roi image over the original slide image
    image[yInit:yEnd, xInit:xEnd] = roi
    
    return image

# Main

# Get all the images from the path
for file in os.listdir(IMAGES_PATH):
    IMAGES.append(os.path.join(IMAGES_PATH, file))

SLIDE_QUEUE = IMAGES.copy()

# Get and remove the first image of the image array
img = cv2.imread(SLIDE_QUEUE.pop(0), cv2.IMREAD_UNCHANGED)

# Get and remove the first image of the image array
img2 = cv2.imread(SLIDE_QUEUE.pop(0), cv2.IMREAD_UNCHANGED)

while True:

    if len(SLIDE_QUEUE) <= 0:
        SLIDE_QUEUE = IMAGES.copy()

    # Resize Image
    imgResized = Resize(img)
    img2Resized = Resize(img2)

    # Add Border
    imgBordered = AddBorder(imgResized)
    img2Bordered = AddBorder(img2Resized)

    # Add Water Mark
    imgWithWaterMark = AddWaterMark(imgBordered)
    img2WithWaterMark = AddWaterMark(img2Bordered)

    cv2.imshow('Slides', imgBordered)

    # Check if q key is pressed and wait 2 seconds before continue
    if cv2.waitKey(CHANGE_IMAGE) & 0xFF == ord('q'):
        break

    # Do the transition
    for alpha in numpy.arange(0, 1, 0.05):
        # Show image
        cv2.imshow('Slides', cv2.addWeighted(imgWithWaterMark, 1-alpha, img2WithWaterMark, alpha, 0))
        
        # Wait 62 ms                
        cv2.waitKey(TRANSITION)    

    # throw away the first image
    img = img2
    # Get and remove the first image of the image array
    img2 = cv2.imread(SLIDE_QUEUE.pop(0), cv2.IMREAD_UNCHANGED)

cv2.destroyAllWindows()