import cv2

cap=cv2.VideoCapture(0)
ret,preview=cap.read()
prev_gray=cv2.cvtColor(preview,cv2.COLOR_BGR2GRAY)
prev_gray=cv2.GaussianBlur(prev_gray,(21,21),0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    frame_diff=cv2.absdiff(prev_gray,gray)

    _,thresh=cv2.threshold(frame_diff,25,255,cv2.THRESH_BINARY)

    thresh=cv2.dilate(thresh,None,iterations=2)
    
    contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c)<1000:
            continue

        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Motion detector",frame)
        cv2.imshow("Threshold",thresh)

        prev_gray=gray

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

cap.release()
cv2.destroyAllWindows()