pattern=["ABABA"]
#find the recursive character
for i in pattern:
    if i in pattern:
        print(pattern)
        break