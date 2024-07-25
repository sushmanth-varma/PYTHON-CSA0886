def findComplement(num):
    mask = 1
    while mask < num:
        mask = (mask << 1) | 1
    return num ^ mask
print(findComplement(5))
print(findComplement(1))
