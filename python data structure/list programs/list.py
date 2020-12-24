num=int(input("enter number"))
lst1=list()
lst2=list()
i=0
for i in range (0,num+1):
    if(i%2==0):
        lst1.append(i)
    elif(i%2!=0):
        lst2.append(i)

print("even list is ",lst1)
print("oddlist is",lst2)