n=int(input("enter the number"))
m=str(n)
a=m[:len(m)//2]
b=m[len(m)//2:]
c=int(a)+int(b)
d=c**2
if d==n:
    print("tech")
else:
    print("non tech")
