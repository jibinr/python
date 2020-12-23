low=int(input("enter lower limit="))
upper=int(input("enter upper limit="))


sum=0
while(low<=upper):
    if(low%2==1):
        sum+=low
    low+=1

print(sum)
