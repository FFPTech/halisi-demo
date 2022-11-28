import cv2
from api import *

cattle_image = cv2.imread('./images/cow_01.png') # read image
image = encodeImage(cattle_image) # encode to base64 string

confidence = 0.45 # choose between 0-1
iou = 0.45 # choose between 0-1
api_key = "" # insert api-key within quotation marks

face = detect(image, api_key, confidence, iou) # run face detection
 
# display detected face 
try :
    img_display = display(cattle_image, face)
    cv2.imshow('Detection', img_display)
    cv2.waitKey(0)
except:
    print('Please inspect input image and retry')