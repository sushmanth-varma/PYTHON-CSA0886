string=input("enter the number")
string1=string.split()[::-1]
print(*string1)
#reverse the striing
num=input("enter the number:")
num1=str(num)
num2=num1[::-1]
print(num2)
if num2==num:
    print("palindrome")



#larges number inn the list
num=[1,2,3,4,5]
largest=num[0]
smaller=num[0]
for number in num:
    if number>largest:
        largest=number
    elif number<largest:
        smaller=number
    
print(largest)
print(smaller)
        
     
  
