import cv2
import base64 as b64
import requests

# function to encode local image as a base64 string
def encodeImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB
    ret, img_enc = cv2.imencode('.jpg', img)
    if not ret:
        return None
    return b64.b64encode(img_enc).decode('utf-8', 'strict')


# function to display detection
def display(img, face, color=(255, 255, 255)):
    img_display = img.copy()
    if face is not None:
        cv2.rectangle(img_display, (face[0], face[1]), (face[2], face[3]), color, thickness=-1)
        img_display = cv2.addWeighted(img, 0.7, img_display, 0.3, 0.0)
    return img_display


def detect(image, api_key, confidence, iou):
    # post API requests
    url = "https://halisi-animal-face-detection.p.rapidapi.com/DetectCow"
    querystring = {"Confidence": str(confidence),"IoU":str(iou)} # choose querystring values between 0-1
    payload = {"image" : image}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key, # ADD YOUR RAPID-API KEY HERE 
        "X-RapidAPI-Host": "halisi-animal-face-detection.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    print(response.text) 
    face = eval(eval(response.text)["bbox"])
    return face