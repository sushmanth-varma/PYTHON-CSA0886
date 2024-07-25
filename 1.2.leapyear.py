y=int(input("enter the anniversary year:"))
if y % 4==0:
    print("anniversary year is leap year")
elif y%100 == 0:
    print("Not a leap year")
elif y%400 == 0:
    print("leap year")

x = y% 4	 
if y % 4 ==0:
       print("nxt anniversary",y+4) 
if y % 4 !=0:
        print("previous year",y-x) 
