def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
nums1_case1 = [1, 2, 3, 0, 0, 0]
m_case1 = 3
nums2_case1 = [2, 5, 6]
n_case1 = 3

merge(nums1_case1, m_case1, nums2_case1, n_case1)
print(nums1_case1)  

nums1_case2 = [1]
m_case2 = 1
nums2_case2 = []
n_case2 = 0

merge(nums1_case2, m_case2, nums2_case2, n_case2)
print(nums1_case2)  
