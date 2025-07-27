num=[2,1,4,3,5]
l=len(num)
for i in range(l):
    su=0
    for j in range(i,l):
        su+=num[j]
print(su)



