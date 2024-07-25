#**A peak element is an element that is strictly greater than its neighbours. Given a 0-
#indexed integer array nums, find a peak element, and return its index. If the array contains
#multiple peaks, return the index to any of the peaks

list=[1,2,3,4,5,6,1]
for i in range(len(list)):
    if i==0 and list[i]>list[i+1]:
        print(i)
        break
    elif i==len(list)-1 and list[i]>list[i-1]:
        print(i)
        break
    elif list[i]>list[i-1] and list[i]>list[i+1]:
        print(i)
        break
#** Find the Mth maximum number and Nth minimum number in an array
#and then find the sum of it, difference of it and product of it

arr = [5, 8, 2, 10, 3]
arr.sort()
m=int(input("enter the maximum num:"))
n=int(input("enter the ma
