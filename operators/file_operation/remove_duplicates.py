f=open("data","r")
set=set()
for item in f:
    set.add(item.rstrip("\n"))
print(set)
#     if item in f:
#         item=1
#         continue
#     else:
#         break
# print(item)
