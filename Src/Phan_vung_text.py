#pip install vietocr

import cv2
import numpy as np
import vietocr

# Khởi tạo mô hình OCR
vocr = vietocr.OCR("vgg_transformer")

# Đọc ảnh thẻ sinh viên
img = cv2.imread("sinhvien.png")

# Chuyển ảnh sang định dạng RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Nhận dạng văn bản trên ảnh
result = vocr.recognize(img_rgb)

# Tạo một dictionary lưu trữ các thông tin được trích xuất
info = {}

# Duyệt qua từng dòng văn bản để tìm kiếm thông tin
for line in result:
    if "Họ và tên" in line[1]:
        info["Họ và tên"] = line[1].replace("Họ và tên", "").strip()
    elif "Ngày sinh" in line[1]:
        info["Ngày sinh"] = line[1].replace("Ngày sinh", "").strip()
    elif "Giới tính" in line[1]:
        info["Giới tính"] = line[1].replace("Giới tính", "").strip()
    elif "Khóa học" in line[1]:
        info["Khóa học"] = line[1].replace("Khóa học", "").strip()
    elif "Hệ" in line[1]:
        info["Hệ"] = line[1].replace("Hệ", "").strip()
    elif "Ngành học" in line[1]:
        info["Ngành học"] = line[1].replace("Ngành học", "").strip()

# In ra các thông tin được trích xuất
print(info)

# Trong đoạn mã trên, chúng ta đầu tiên khởi tạo một đối tượng OCR với mô hình vgg_transformer. 
# Sau đó, chúng ta đọc ảnh thẻ sinh viên và chuyển đổi nó sang định dạng RGB. Tiếp theo, chúng ta 
# sử dụng đối tượng OCR để nhận dạng văn bản trên ảnh và lưu kết quả vào biến result.

# Sau đó, chúng ta tạo một dictionary lưu trữ các thông tin được trích xuất và duyệt qua từng dòng 
# văn bản để tìm kiếm thông tin. Nếu một dòng văn bản chứa thông tin về một trường nào đó, chúng ta 
# sẽ trích xuất