a=int(input())
b=int(input())
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(i)
                break
count=0
n=int(input("enter the number: "))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("it is a prime")
else:
    print("not prime")

                
y=int(input("enter the anniversary year:"))
