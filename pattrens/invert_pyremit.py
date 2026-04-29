"""n=6

for i in range(n):
    for a in range(0,i+1):
         print("1",end=" ")
    for j in range(0,n-i):
        print("*",end=" ")

    

    print()"""


n = 5
for i in range(n, 0, -1):
    print("1"*(n-i) + "*2"*i)