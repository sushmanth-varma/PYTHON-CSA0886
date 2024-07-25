def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1
print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))  

