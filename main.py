n=4
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end = "")
    for k in range(2*i-1):
        if i==1 or i==n or k==0 or k==(2*i-1)-1:
            print("*",end= "")
        else:
            print(" ",end ="")
    print()
        