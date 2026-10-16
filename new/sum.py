a=[1,2,3,4,5]

t=7

for i in range(len(a)+1):
    for j in range(i+1):
        if a[i]+a[j] == t:
            print(i,j)