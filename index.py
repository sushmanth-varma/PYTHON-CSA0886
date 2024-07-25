string=input("enter the string")
char=input("enter the charetere:")
index=-1
for i in range(len(string)):
    if string[i]==char:
        index=i
        break
if index!=-1:
    print("index is:",index)
else:
    print("not found")


word=input("enter the word:")
sorted_word=''.join(sorted(word))
print("sorted in normal word",sorted_word)
reverse_sorted_word=''.join(sorted(word,reverse=True))
print("the reverse sorted word",reverse_sorted_word)
