a=int(input("enter the number"))
b=int(input("enter the number"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
        if count==2:
            print("it is a prime")
            
#prime in range
            a=int(input("enter the number:"))
            b=int(input("enter the number:"))
            for i in range(a,b+1):
                if i>1:
                    for j in range(2,i):
                        if i%j==0:
                            print(i)
                            break
            a=int(input("enter the number:"))
            b=int(input("enter the number:"))
            for i in range(a,b+1):
                count=0
                for j in range(2,i):
                    if i%j==0:
                        count=1
                        break
                    if count==0:
                        print(i)
                        break


                    n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
for i in range (n1,n2+1):
    if i>1:
        fact=0
        for j in range(1,i):
            if i%j==0:
                fact=fact+1
    
        if fact==1:
            print(i)
