def removeDuplicates(nums):
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    return k

# Test cases
nums1 = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums1), nums1[:removeDuplicates(nums1)])  # Output: 5, [1, 1, 2, 2, 3]

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums2), nums2[:removeDuplicates(nums2)])  # Output: 7, [0, 0, 1, 1, 2, 3, 3]
########
def search(nums, target):
    return target in nums
print(search([2, 5, 6, 0, 0, 1, 2], 0))
print(search([2, 5, 6, 0, 0, 1, 2], 3))
def grayCode(n):
    result = [0]
    for i in range(n):
        result += [x + 2**i for x in reversed(result)]
    return result
print(grayCode(2))
print(grayCode(1))
####
def subsetsWithDup(nums):
    res = [[]]
    nums.sort()
    prev = -1
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            start = prev
        else:
            start = 0
        prev = len(res)
        res += [curr + [num] for curr in res[start:]]
    return res

# Test cases
print(subsetsWithDup([1, 2, 2]))  # Output: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
print(subsetsWithDup([0]))  # Output: [[], [0]]
#####
def numDecodings(s):
    if not s or s[0] == '0': return 0
    dp1, dp2 = 1, 1
    for i in range(1, len(s)):
        dp = 0
        if s[i] != '0': dp += dp2
        if 10 <= int(s[i-1:i+1]) <= 26: dp += dp1
        dp1, dp2 = dp2, dp
    return dp2

# Test cases
print(numDecodings("12"))  # Output: 2
print(numDecodings("226"))  # Output: 3
