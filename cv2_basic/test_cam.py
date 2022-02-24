import cv2

cam=cv2.VideoCapture(rtsp://admin:admin123@192.168.29.30:554/cam/realmonitor?channel=1&subtype=1)

while True:
	
    _,img=cam.read()
    
    cv2.imshow("TEST",img)
    
    cv2.waitKey(1)