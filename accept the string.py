string=input("enter the string:")
vowels="aeiouAEIOU"
new_string=""
for char in string:
    if char in vowels:
        pass
    else:
        new_string=new_string+char
print(new_string)
