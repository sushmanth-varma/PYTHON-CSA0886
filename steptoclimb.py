s=int(input("enter the number"))
a,b=0,1
if s<1:
    print(s)
else:
    for i in range(2,s+2):
        fib=a+b
        a,b=b,a+b
    print(fib)
        
