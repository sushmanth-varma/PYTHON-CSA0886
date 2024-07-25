a='1111'
b='1110'
c='1100'
bina=int(a,2)
binb=int(b,2)
binc=int(c,2)
if bina>binb and bina>binc:
    print("a is greater",a)
elif binb>bina and binb>binc:
    print("b is greater",b)
else:
    print("c is greater",c)
