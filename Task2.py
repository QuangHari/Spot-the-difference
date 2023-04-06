import cv2
import imutils
import numpy as np

# Đọc 2 ảnh đầu vào và resize cho phù hợp
img1 = cv2.imread('C:\FilePNG\img1.jpg')
img1 = cv2.resize(img1, (400, 500))
img2 = cv2.imread('C:\FilePNG\img1Lv2.jpg')
img2 = cv2.resize(img2, (400, 500))

# Tạo ra 1 ảnh chứa điểm khác biệt từ 2 ảnh
diff = cv2.subtract(img1, img2)
# Chuyển sang Grayscale và áp dụng threshold
diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(diff_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Từ threshold ở trên ta áp dụng dilate để các điểm khác biệt to ra
kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations=5)


# Tìm viền của các vùng khác biệt
contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Vẽ hình vuông bao quanh các điểm khác biệt
for contour in contours:
    if cv2.contourArea(contour) > 100:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Ghép 2 ảnh lại và hiện ra kết quả
result = np.hstack((img1, img2))
cv2.imshow('Difference', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
