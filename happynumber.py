n=int(input("enter the number"))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum+=r**2
        x=x//10
    x=sum
if x==1:
    print("happy")
else:
    print("not happy")
