def ar(item):

    a=[]

    for i in item:
        if isinstance(i,list):
            a.extend(ar(i))

        else:
            a.append(i)

    return a


d= [[[1, 2], 2, 3, 4, 5], 4, [4]]
print(ar(d))
