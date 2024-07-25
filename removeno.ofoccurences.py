def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
nums1 = [3, 2, 2, 3]
val1 = 3
print(removeElement(nums1, val1))  
nums2 = [0, 1, 2, 2, 3]
val2 = 2
print(removeElement(nums2,val2)) 
