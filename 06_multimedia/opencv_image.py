import cv2

img  = cv2.imread('style_607e47641bf38.jpg')
img2 = cv2.resize(img, (1000,800))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

edge1 = cv2.Canny(img, 50,100)
edge2 = cv2.Canny(img, 100,150)
edge3 = cv2.Canny(img, 150,200)

#cv2.imshow('TWICE',img)
#cv2.imshow('TWICE1-1',img2)
#cv2.imshow("TWICE2", gray)
cv2.imshow('TWICE1',edge1)
cv2.imshow('TWICE2',edge2)
cv2.imshow('TWICE3',edge3)

cv2.waitKey(0)
#while True:
    #if cv2.waitKey() == 13:
        #cv2.imwrite('TWICE_GRAY.jpg', gray)
        #break;

cv2.destroyAllWindows()