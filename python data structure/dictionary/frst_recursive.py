pattern="abcdeff"
dict={}
for item in pattern:
    if item in dict:
        print("firstrecursie charis",item)
        break
    else:
        dict[item]=1


