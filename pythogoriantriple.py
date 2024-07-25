limit=int(input("enter the limit"))
triples=[(a,b,c) for a in range(1,limit) for b in range(1,limit) for c in range(1,limit) if a**2+b**2==c**2]
print("triples")
for triple in triples:
    print(triple)
