import re
from googletrans import Translator


# Dòng chứa thông tin sinh viên
student_info = "Full name: BUI HUY HOANG\nDoB\n11/12/2003\nGender: Male\nIntake\n2021-2024\nCourse: Bachelor\nMajor\nInformation and Communication\nTechnology\nBI12-170\nValidity: 30/10/2024"

# Tìm và ghép các phần của đối tượng lại với nhau
full_name = re.search(r"Full name: (.+)", student_info).group(1)
dob = re.search(r"DoB\n(.+)", student_info).group(1)
gender = re.search(r"Gender: (.+)", student_info).group(1)
intake = re.search(r"Intake\n(.+)", student_info).group(1)
course = re.search(r"Course: (.+)", student_info).group(1)
major = re.search(r"Major\n(.+)\n", student_info).group(1)
validity = re.search(r"Validity: (.+)", student_info).group(1)

# Lưu thông tin vào biến student_info_oneline
student_info_oneline = f"Full Name: {full_name}\nGender: {gender}\nDate of Birth: {dob}\nCourse: {course}\nIntake: {intake}\nMajor: {major}\nValidity: {validity}"

translator = Translator()

# Dịch sang tiếng Việt
result_vi = translator.translate(
    student_info_oneline, src='en', dest='vi').text

# Dịch sang tiếng Pháp
result_fr = translator.translate(
    student_info_oneline, src='en', dest='fr').text

# Hiển thị kết quả dịch

# Hiển thị biến student_info_oneline
print(student_info_oneline)
print('Thông tin sinh viên (Tiếng Việt):')
print(result_vi)
print('Thông tin sinh viên (Tiếng Pháp):')
print(result_fr)
