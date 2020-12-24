#find least positive missing integer -2 -1 0 1 2 3 4
list=[-2,-1,0,2,3]
count=1
for num in range(0,len(list)):
    if count in list:
        count+=1
        pass
    else:
        print(count,"is least postvenumber")
        break
