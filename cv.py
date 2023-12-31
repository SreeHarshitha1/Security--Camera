import cv2
import winsound
cap=cv2.VideoCapture(0) #// if you have second camera you can set first parameter as 1
if not (cap.isOpened()):
    print("Could not open video device")
while True:
    ret,frame1= cap.read()
    ret, frame2 = cap.read()
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1,contours,-1,(0,255,0),0)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        winsound.playsound('alert.wav', winsound.SND_ASYNC)




    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Live",frame1)
cv2.destroyAllWindows()
