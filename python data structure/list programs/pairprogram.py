list=[2,1,3,4,6,7]
list.sort()
#1 2 3 4 6 7
low=0
upper=len(list)-1
element=int(input("enter value"))
while(low<upper):
    total=list[upper]+list[low]
    if(element<total):
        upper-=1
    elif(element>total):
        low+=1
    elif(element==total):
        print("pairs are",list[upper],",",list[low])
        break
    else:
        break
# # print(list)
# sorted(list)
# print(list3)
# employees=[[1000,"ajay","qa",1981,2333],[1002,"vijay","dev",1992,2008],[1003,"arun","ba",1989,2010],[1004,"amal","dev",2009,1989]]
# out=[]
# for i in employees:
#
#     if i[2] not in out:
#         out.append(i[2])
# # print(out)
# for i in out:
#     print (i)
#         # if i not in out:
        #     out.append()




