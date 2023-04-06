import cv2

# đọc ảnh và chuyển sang ảnh xám
img = cv2.imread('C:\FilePNG\img1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Canny
edges = cv2.Canny(gray, 100, 200)
# Tìm các đường viền
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if 800 <= area <= 1400:  # Chọn contour có độ lớn phù hợp
        cv2.drawContours(img, contours, i, (0, 255, 255), 2) # Vẽ viền màu vàng

# hiển thị ảnh và lưu kết quả
cv2.imshow('result', img)
cv2.imwrite('C:\FilePNG\img1Lv2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()