list=[1,2,3,4,5,6,7,8,9]
result=[]
for num in list:
    fact=0
    for i in range(1,num):
        if num%i==0:
            fact=fact+1
    if fact>2:
        result.append(num)
print("composite numbers",result)
print("composte numbers",len(result))


#composite non
list=[1,2,3,4,5,6,7,8,9]
result=[]
for num in list:
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact=fact+1
    if fact==0:
        result.append(num)
print("composite numbers",result)
print("composte numbers",len(result))
#lines
f=input("enter")
c=0
for x in f:
    print(x,end=" ")
    c=c+1
    print(c,end="")
