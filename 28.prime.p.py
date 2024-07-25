count=0
n=int(input("enter the number: "))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("it is a prime")
else:
    print("not prime")
