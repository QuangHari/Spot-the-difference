import cv2
import random

# Đọc ảnh đầu vào và resize cho phù hợp
img = cv2.imread('C:\FilePNG\img1.jpg')
img = cv2.resize(img, (400, 500))

# Random các tọa độ ảnh
y1 = random.randint(50, 350)
x1 = random.randint(50, 450)
# Random mã màu và vẽ
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
cv2.rectangle(img, (y1, x1), (y1 + 50, x1 + 50), (b, g, r), -1)


y2 = random.randint(50, 350)
x2 = random.randint(50, 450)
# Đảm bảo 2 điểm tọa độ được sinh ra không quá gần hay trùng nhau
while x1 + 50 > x2 > x1 - 50:
    x2 = random.randint(50, 450)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
cv2.circle(img, (y2, x2), 30, (b, g, r), -1)

# Xem và lưu kết quả
cv2.imwrite('C:\FilePNG\img1Lv1.jpg', img)
cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
