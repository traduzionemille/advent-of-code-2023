f = open("input1.txt", "r")
calibration_document = (f.readlines())

calibration_values = []

for item in calibration_document:
    digits = []
    for element in item:
        if element.isdigit():
            digits.append(element)
    value = digits[0] + digits[-1]
    calibration_values.append(int(value))

total_calibration_value = sum(calibration_values)
print("The sum of all of the calibration values is: ", total_calibration_value)