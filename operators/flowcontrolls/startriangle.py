#       *
#   *       *
#*  *   *   *   *
# n=int(input("nter value for n "))
# for row in range(1,n+1):
#     for col in range(1,(2*row-1)):
#         print("*",end=" ")
#     print()
for row in range(1,5):
    for col in range(1,8):
        if(row+col==5 or row==4 or col-row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()