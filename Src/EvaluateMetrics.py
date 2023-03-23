import Levenshtein

# Original
#reference = "Full name: BUI HUY HOANG\nDoB: 11/12/2003\tGender: Male\nIntake: 2021-2024\tCourse: Bachelor\nMajor: Information and Communication\nTechnology\n\nBI12-170\nValidity: 30/10/2024"

#reference = "Họ và tên: LẠI HẢI ANH\nNgày sinh: 15/01/2002 Giới tính: Nữ\nKhóa học: 2020-2024 Hệ:Cử nhân\nNgành học: An toàn thông tin\n\nBA11-004 \nHSD: 31/10/2024"

#reference = "Full name: PHAM DUC ANH\nDoB: 30/09/2002 Gender: Male\nIntake: 2020-2023 Course: Bachelor\nMajor: Information Technology and Communication\n\nBI11-021\nValidity: 31/10/2023"
#reference = "Full name: NGUYEN DUC MINH\nDoB: 14/03/2002 Gender: Male\nIntake: 2020-2023 Course: Bachelor\nMajor: Information Technology and Communication\n\nBI11-163\nValidity: 31/10/2023"
#reference = "Họ và tên: NGUYỄN ĐỨC MINH\nNgày sinh: 14/03/2002 Giới tính: Nam\nKhóa học: 2020-2023 Hệ:Cử nhân\nNgành học: Công nghệ thông tin và Truyền thông"
reference ="Họ và tên:TRẦN NGỌC BÁCH\nNgày sinh:11/12/2001  Giới tính:Nam\nHệ đào tạo:CỬ NHÂN    Khóa: 2019-2023\nNgành:CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG\n\nMSV:BA10-004"


# Genereated by Tesseract OCR
#hypothesis = "Họ và tên: LẠI HẢI ANH\n\nNgày sinh: 15/01/2002 Giới tinh: Nar\nKhóa học: 2020-2024 Hệ:Cử nhân\nNgành học: An toàn thông tin\n\nBA11-004 4\nHSD: 31/10/2024 :r ]"
#hypothesis = "Full name:PHAM DUC ANH\n\nDoB: 30/09/2002 Gender: Male\nIntake: 2020-2023 Course: Bachelor\nMajor: Information Technology and Communication\n\nBI11-021\n\nValidity: 31/10/2023\n7 d"
#hypothesis = "Full name:NGUYEN DUC MINH\n\nDoB: 14/03/2002 Gender: Male\nIntake: 2020-2023 Course: Bachelor\nSN Major: —_[nformation Technology and Communication\n\nBI11-163\n\nValidity: 31/10/2023"
#hypothesis = "BI1-163\nHSD: 31/10/2023\n\nTHẺ SINH VIÊN\n\nHọ và tên: NGUYÊN ĐỨC MINH\n\nNgày sinh: 14/03/2002 Giới tính:Nam\nKhóahọc: 2020-2023. Hệ:Cử nhân\nNgành học: Công nghệ thông tin và Truyền thông"
hypothesis = "Họ và tên: TRAN NGOC BACH\nNgày sinh: 11/12/2001 Giới tính: Nam\nHệ đào tạo: CỦ NHÂN Khóa: 2019-2023\n\nNgành: CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG\n\nxsv.sasss - ||||INIIWIIM"


# calculate WER
wer = Levenshtein.distance(reference.split(), hypothesis.split()) / len(reference.split())

# calculate CER
cer = Levenshtein.distance(reference.replace(' ', '').replace('\n', ''), hypothesis.replace(' ', '').replace('\n', '')) / len(reference.replace(' ', '').replace('\n', ''))

print("WER:", wer)
print("CER:", cer)
