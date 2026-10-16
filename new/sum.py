"""a=[1,2,3,4,5]

t=7

for i in range(len(a)):
    for j in range(i+1):
        if a[i]+a[j] == t:
            print(i,j)"""


def sum(a,t):
    seen={}

    for i,n in enumerate(a):

        c=t-n

        if c in seen:
            return [seen[c],i]

        seen[n]=i


a=[2,7,11,15]
t=9
print(sum(a=a,t=t))