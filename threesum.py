n=[10,2,3,4,6]
t=15

for i in range(len(n)):
    for j in range(i+1,len(n)):
        for h in range(j+1,len(n)):
            if t == n[i]+n[j]+n[h]:
                print(i,j,h)