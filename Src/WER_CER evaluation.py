# nhập danh sách giá trị WER và CER
wer_list = list(map(float, input("Nhập danh sách giá trị WER, các giá trị cách nhau bởi khoảng trắng: ").split()))
cer_list = list(map(float, input("Nhập danh sách giá trị CER, các giá trị cách nhau bởi khoảng trắng: ").split()))

# tính giá trị trung bình của WER và CER
wer_mean = sum(wer_list) / len(wer_list)
cer_mean = sum(cer_list) / len(cer_list)

# in ra giá trị trung bình của WER và CER
print(f"Giá trị trung bình của WER: {wer_mean}")
print(f"Giá trị trung bình của CER: {cer_mean}")

# so sánh giá trị trung bình với tiêu chuẩn và quy chuẩn chung
if wer_mean < 0.1 and cer_mean < 0.1:
    print("Model OCR rất tốt")
elif wer_mean < 0.3 and cer_mean < 0.3:
    print("Model OCR tốt")
elif wer_mean < 0.5 and cer_mean < 0.5:
    print("Model OCR khá tốt")
else:
    print("Model OCR còn phải cải thiện") 
