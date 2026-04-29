n=6

for i in range(n):
    for j in range(0,n-i):
        print("*",end=" ")

    for a in range(0,i+1):
        print("1",end=" ")

    print()