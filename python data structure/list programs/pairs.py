list=[1,2,3,4,6]#value=6 find sum pairs

value=6
for num in list:
    for num1 in list:

        if(value==num+num1):
            print(num,num1)
            break
