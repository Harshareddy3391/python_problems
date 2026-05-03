arry=[1,2,3,4,3,2]


seen=set()
dup=set()


for i in arry:

    if i not in seen:
        seen.add(i)
    else:
        dup.add(i)

print(list(seen))
print(arry)
print(list(dup))