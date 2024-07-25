n=int(input())
fact=1
sum=0
if n<0:
    print("invalid")
elif n==0:
    print("0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
        sum+=fact/i
        print(int(sum))
