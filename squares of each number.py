def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] * nums[left]
            left += 1
        else:
            result[index] = nums[right] * nums[right]
            right -= 1
        index -= 1
    
    return result
nums_case1 = [-4, -1, 0, 3, 10]
print(sortedSquares(nums_case1))  
nums_case2 = [-7, -3, 2, 3, 11]
print(sortedSquares(nums_case2))
