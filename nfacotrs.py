n=int(input("enter the number:"))
list=[]
for i in range(1,n+1):
    if n%i==0:
        list.append(i)
print(list)
length=len(list)
print("number of factors:",length)
x=int(input("enter the number:"))
for i in range(0,x):
    if x>length:
        print("invalid")
        break
    else:
        print(list[i],end=" ")
