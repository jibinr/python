pattern="ababa"
lst=list(pattern)
#find the recursive character
for i in lst:
    if i in lst[lst.index(i)+1:]:
        print(i)
        break