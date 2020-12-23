num1=int(input("num1"))
num2=int(input("num3"))
num3=int(input("num3"))
if(num1>=num2&num1>=num3):
    print(num1," is big")
elif(num2>=num1&num2>=num3):
    print(num2,"is big")
elif(num3>=num1&num3>=num2):
    print(num3,"is big")
else:
    print("invalid")