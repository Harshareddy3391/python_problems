"""for i in range(1,7):

    for j in range(i):
        print("1"*j,"*",end="")
    print()
"""


n=6 
"""
for i in range(1,n+1):
    for j in range(0,n-i):
        print("",end=" ")

    for k in range(0,i):
        print("*",end=" ")

    print()"""



for i in range(0,n):
    for j in range(0,n-i):
         print(end=" ")
    for a in range(0,i):
        print("*",end=" ")
    print()