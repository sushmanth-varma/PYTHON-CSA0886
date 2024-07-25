n=[3,2]
distict_num=list(set(n))
distict_num.sort(reverse=True)
if len(distict_num)>=3:
    print(distict_num[2])
else:
    print(distict_num[0])



#hbvjhfbvghvb




nums = [1, 1, 0, 1, 1, 1]  # Replace with your input

max_consecutive = 0
current_consecutive = 0

for num in nums:
    if num == 1:
        current_consecutive += 1
        if current_consecutive > max_consecutive:
            max_consecutive = current_consecutive
    else:
        current_consecutive = 0

print(max_consecutive)
#ksfvjnvdfj
num = 5  # Replace with your input

binary_rep = bin(num)[2:]  # Get binary representation without '0b' prefix
complement = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
complement_num = int(complement, 2 )
print(complement_num)

#kdmejfnfrdjn
x = 1  # Replace with your input
y = 4  # Replace with your input

x_bin = format(x, 'b')
y_bin = format(y, 'b')

# Pad the shorter binary number with leading zeros
max_len = max(len(x_bin), len(y_bin))
x_bin = x_bin.zfill(max_len)
y_bin = y_bin.zfill(max_len)

hamming_distance = sum(1 for xb, yb in zip(x_bin, y_bin) if xb != yb)
print(hamming_distance)
#ksdjfsejfndsn
nums = [4, 3, 2, 7, 8, 2, 3, 1]  # Replace with your input

n = len(nums)
all_numbers = set(range(1, n + 1))
nums_set = set(nums)

missing_numbers = list(all_numbers - nums_set)
print(missing_numbers)


