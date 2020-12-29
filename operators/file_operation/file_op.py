#file operations read write append
#inorder to get namesfrom names
# step1 create reference
# reference_name=open(filepath,mode_of_operations)
f=open("names","r")
lst=[]

for item in f:

    lst.append(item.rstrip("\n"))
print(lst)
# rstrip or lstrip
# data="hello \n"
# data=data.rstrip("\n")
# print(data)