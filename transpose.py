


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
rows=len(a)
cols=len(a[0])
t=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(0,cols):
    for j in range(0,rows):
        t[i][j]=a[j][i]
        print(t[i][j],end=" ")
    print(" ")
