string1=input("enter the string:")
string2=input("enter the string:")
count=0
for char1,char2 in zip(string1,string2):
    if char1==char2:
        count=count+1
print(count)
