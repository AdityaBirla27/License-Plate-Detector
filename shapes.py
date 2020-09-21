import cv2

img = cv2.imread('lena.jpg',-1)

cv2.line(img,(0,0),(255,255),(255,0,0),3)

cv2.rectangle(img,(0,0),(255,255),(0,255,0),3)

cv2.putText(img,'IEEE',(255,255),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),5,cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()