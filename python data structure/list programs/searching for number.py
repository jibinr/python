list=[120,11,12,13,14]
element=int(input("enter the element"))

if (element in list):

    print("element found at index position",list.index(element))
else:
    print("not found")
