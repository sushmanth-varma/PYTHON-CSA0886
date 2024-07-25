
stmt=input("enter the string:")
x='aeiouAEIOU'
y='qwrtyplkjhgfdsazxcvbnmQWRTYPLKJGFDSAZXCVBNM'
vowels=0
consonants=0
for char in stmt:
    if char in x:
        vowels=vowels+1
    elif char in y:
        consonants=consonants+1
    else:
        pass
         
         
print("number of vowels:",vowels)
print("number of cosonants:",consonants)
if vowels>consonants:
    print("vowels are maximum")
elif vowels<consonants:
    print("consonants are maximum")
else:
    print("vowels and consonants are same")
