text="hello hai hello hello hai hai hmm"
words=text.split(" ")
dict={}
for item in words:
    if (item in dict):
        dict[item]+=1
    else:
        dict[item]=1
print(dict)
#     for item2 in words:
#         if item in words:
#
#             count+=1
# print(count)
