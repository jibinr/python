f=open("word_data","r")
# count=0
dict={}
for item in f:
    word=item.rstrip("\n").split(" ")
    for word in item:
        word=word.rstrip("")
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
for k,v in dict.items():
    print(k,v)