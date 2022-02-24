import cv2

cam=cv2.VideoCapture('rtsp://admin:12345@172.16.53.204:554/cam/realmonitor?channel=1&subtype=1')
test_On = True

while test_On:
    
    _,img=cam.read()
    
    cv2.imshow("TEST",img)
    
    cv2.waitKey(1)











