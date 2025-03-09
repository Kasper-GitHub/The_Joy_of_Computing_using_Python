#Image enhancement CLAHE
import cv2

#Read the image
img = cv2.imread('Scene.png')

#Preparation for CLAHE
clahe = cv2.createCLAHE()

#Convert to gray scale image 40
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply enhancement
enh_img = clahe.apply(gray_img)

# save it to a file
cv2.imwrite('enhanced.png', enh_img)

print('Done enhancing')