list=[6,6,8,9,4,2,3]#[7,7,9,10,3,1,2
out=[]
for num in list:
    if(num>5):
        num=num+1
        out.append(num)
    elif(num<5):
        num=num-1
        out.append(num)
print(out)
