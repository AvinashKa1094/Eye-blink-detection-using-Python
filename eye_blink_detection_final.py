import numpy as np
import cv2
face = cv2.CascadeClassifier('D://codespeedy//haarcascades//haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('D://codespeedy//haarcascades//haarcascade_eye.xml')
snap = cv2.VideoCapture(0)
while 1:
    ret, img = snap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    for (left,right,upper,down) in faces:
        cv2.rectangle(img,(left,right),(left+upper,right+down),(255,0,0),2)
        roi_gray = gray[right:right+down, left:left+upper]
        roi_color = img[right:right+down, left:left+upper]
        
        eyes = eye.detectMultiScale(roi_gray)
        for (E_left,E_right,E_upper,E_down) in eyes:
            cv2.rectangle(roi_color,(E_left,E_right),(E_left+E_upper,E_right+E_down),(0,255,0),2)

    cv2.imshow('img',img)
    esc = cv2.waitKey(30) & 0xff
    if esc == 27:
        break

cap.release()
cv2.destroyAllWindows()
