#
# i=2
# for i in range(10,50):
#     if(10%i==0):
#         i+=1
#         break
#     else:
#         print (i)
# for i in range(1,13):
    # if(i%4==0):
    #     print(i)
    # else:
    #     print(i,end="\t")
    # print(i,end=" ")

#*
#**
#***
#****
#n=int(input("enter value for n"))
# for row in range(0,n+1):
#     for col in range(0,row):
#         print("*",end=" ")
#     print()
#1
# 12
# 123
# 1234
n=int(input("enter thevaluefor n "))
for row in range(0,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()