import Levenshtein

# đoạn văn bản gốc
#reference = "Full name: BUI HUY HOANG\nDoB: 11/12/2003\tGender: Male\nIntake: 2021-2024\tCourse: Bachelor\nMajor: Information and Communication\nTechnology\n\nBI12-170\nValidity: 30/10/2024"

# đoạn văn bản
reference = "Họ và tên: LẠI HẢI ANH\nNgày sinh: 15/01/2002 Giới tính: Nữ\nKhóa học: 2020-2024 Hệ:Cử nhân\nNgành học: An toàn thông tin\n\nBA11-004 \nHSD: 31/10/2024"

# đoạn văn bản được nhận diện bởi Tesseract OCR
hypothesis = "Họ và tên: LẠI HẢI ANH\n\nNgày sinh: 15/01/2002 Giới tinh: Nar\nKhóa học: 2020-2024 Hệ:Cử nhân\nNgành học: An toàn thông tin\n\nBA11-004 4\nHSD: 31/10/2024 :r ]"


# tính WER
wer = Levenshtein.distance(reference.split(), hypothesis.split()) / len(reference.split())

# tính CER
cer = Levenshtein.distance(reference.replace(' ', '').replace('\n', ''), hypothesis.replace(' ', '').replace('\n', '')) / len(reference.replace(' ', '').replace('\n', ''))

print("WER:", wer)
print("CER:", cer)
