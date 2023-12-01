f = open("input1.txt", "r")
calibration_document = (f.readlines())

calibration_values = []
new_calibration_document = []
newest_calibration_document =[]

spelled_out_digits = {'one': '1', 'two': '2', 'three': '3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight': '8', 'nine':'9'}

for item in calibration_document:
    for key, value in spelled_out_digits.items():
        if key in item:
            item = item.replace(key, key + key[-1])
    new_calibration_document.append(item)

for item in new_calibration_document:
    for key, value in spelled_out_digits.items():
        if key in item:
            item = item.replace(key, value)
    newest_calibration_document.append(item)

print(newest_calibration_document)

for item in newest_calibration_document:
    digits = []
    for element in item:
        if element.isdigit():
            digits.append(element)
    value = digits[0] + digits[-1]
    calibration_values.append(int(value))

total_calibration_value = sum(calibration_values)
print("The sum of all of the calibration values is: ", total_calibration_value)