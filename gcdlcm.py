n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
t1=n1
t2=n2
while n1%n2!=0:
    r=n1%n2
    n1=n2
    n2=r
    gcd=n2
    print(gcd)
    lcm=n1*n2
    print(lcm)
