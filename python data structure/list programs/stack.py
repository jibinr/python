# nestedlist
employees=[[1000,"ajay","qa",1981,2333],[1002,"vijay","dev",1992,2008],[1003,"arun","ba",1989,2010],[1004,"amal","dev",2009,1989]]
# for num in employees:
#     print(num[0],num[1])
element=str("dev")
count=0
for num in employees:
    if num[2]==element:
        count+=1

print(count)