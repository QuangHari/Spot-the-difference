import cv2
import numpy as np
import random
# đọc ảnh và thay đổi kích cỡ
img = cv2.imread('C:\FilePNG\img1.jpg')
img = cv2.resize(img, (400, 500))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Lọc các màu trong khoảng low ,high
low = np.array([120, 120, 120])
high = np.array([255, 255, 255])
mask = cv2.inRange(img_rgb, low, high)  #Áp threshold trong 2 khoảng màu

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    if 1000 > cv2.contourArea(contour) > 500:  # Chọn độ lớn contour
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cv2.fillPoly(img, [contour], (b, g, r))

cv2.imwrite('C:\FilePNG\img1lv3.jpg', img)
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
