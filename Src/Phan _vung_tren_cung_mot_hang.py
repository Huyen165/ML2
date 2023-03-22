import cv2
import numpy as np
import vietocr

# Khởi tạo mô hình OCR
vocr = vietocr.ocr.OCR("vgg_transformer")

# Đọc ảnh thẻ sinh viên
img = cv2.imread("test3.jpg")

# Chuyển ảnh sang định dạng grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Gauss để làm mờ ảnh
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Phát hiện biên cạnh trên ảnh
edges = cv2.Canny(blur, 50, 150, apertureSize=3)

# Tìm các đường viền trên ảnh
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Lặp qua các đường viền để tìm vùng chứa các trường
for contour in contours:
    # Tính diện tích của đường viền
    area = cv2.contourArea(contour)
    # Nếu diện tích đường viền nhỏ hơn một ngưỡng thì bỏ qua
    if area < 1000:
        continue
    # Lấy hình chữ nhật bao quanh đường viền
    x, y, w, h = cv2.boundingRect(contour)
    # Chia vùng bao quanh đường viền thành các ô vuông bằng nhau
    size = int(w / 3)
    for i in range(3):
        for j in range(2):
            # Tạo một vùng chứa các trường
            roi = img[y+j*size:y+(j+1)*size, x+i*size:x+(i+1)*size]
            # Nhận dạng văn bản trên vùng chứa các trường
            result = vocr.recognize(roi)
            # Duyệt qua từng dòng văn bản
        for line in result:
            # Kiểm tra xem dòng văn bản chứa thông tin về ngày sinh và giới tính hay không
            if "Ngày sinh:" in line:
                # Nếu có, tách dòng văn bản đó thành các phần riêng lẻ
                parts = line.split()
                # Lấy thông tin về ngày sinh và giới tính
                ngaysinh = " ".join(parts[2:5])
                gioitinh = parts[-1]
                print("Ngày sinh: ", ngaysinh)
                print("Giới tính: ", gioitinh)
            # Kiểm tra xem dòng văn bản chứa thông tin về khóa học và hệ đào tạo hay không
            elif "Khóa học:" in line:
                # Nếu có, tách dòng văn bản đó thành các phần riêng lẻ
                parts = line.split()
                # Lấy thông tin về khóa học và hệ đào tạo
                khoahoc = parts[2]
                he = parts[4]
                print("Khóa học: ", khoahoc)
                print("Hệ: ", he)
            else:
                # Nếu không, in ra toàn bộ dòng văn bản
                print(line)
                


