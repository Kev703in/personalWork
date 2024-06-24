list=[1,4,2,5,7,8,4,9,5,7,6,2,8,9,4,3]
print(f"initial list\n{list}")
#list.sort()
#print(list)
#y=list[0]
#z=[]
#z.append(y)
#for x in range(1,len(list)-1):
#    if list[x] != y:
#        z.append(list[x])
#    y=list[x]
#print(z)

x=[]

for nu in list:
    if nu not in x:
        x.append(nu)
print(x)