import cv2
import random
img = cv2.imread('Assets/logo.jpg',1)
#print(img.shape)
#tag = img[100:200,400:600]
#img[0:100,200:400] = tag
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()