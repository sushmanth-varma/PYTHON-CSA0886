marks=int(input("enter the marks:"))
if marks>=90:
       result =  'a'
elif 80<=marks<90:
       result=  'b'
elif 70<=marks<80:
       result=  'c'
elif 60<=marks<70:
       result= 'd'
else:
    result= 'f'
print(marks,result)
