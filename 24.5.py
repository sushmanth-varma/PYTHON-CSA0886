digits = [1, 2, 3]
for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        break
    digits[i] = 0
else:
    digits.insert(0, 1)
print(digits)
