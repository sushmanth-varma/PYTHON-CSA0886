arr=[2,7,4,5,8,9,10]
arr.sort()
m=int(input("enter the number"))
n=int(input("enter the min number"))
min_num=arr[n-1]
max_num=arr[len(arr)-m]
print("minumum number is:",min_num)
print("max number is :",max_num)
sum=max_num+min_num
dif=max_num-min_num
product=max_num*min_num
print("sum is:",sum)
print("difference is:",dif)
print("product is:",product)
            
