# Enter the list of WER and CER values
wer_list = [0.19047619047619047, 0.19047619047619047, 0.3333333333333333, 0.19230769230769232]
cer_list = [0.033783783783783786, 0.033783783783783786, 0.033783783783783786, 0.059322033898305086]

# Calculate the mean values of WER and CER
wer_mean = sum(wer_list) / len(wer_list)
cer_mean = sum(cer_list) / len(cer_list)

# Print out the mean values of WER and CER
print(f"Mean value of WER: {wer_mean}")
print(f"Mean value of CER: {cer_mean}")

# Compare the mean values with the standard criteria
if wer_mean < 0.1 and cer_mean < 0.1:
    print("The OCR model is very good")
elif wer_mean < 0.3 and cer_mean < 0.3:
    print("The OCR model is good")
elif wer_mean < 0.5 and cer_mean < 0.5:
    print("The OCR model is quite good")
else:
    print("The OCR model needs improvement")
