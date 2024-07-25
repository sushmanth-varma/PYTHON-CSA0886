n=int(input("enter the numeber:"))
d=1
while d<=n:
    if n%d==0:
        print(d,end="")
        d+=1
