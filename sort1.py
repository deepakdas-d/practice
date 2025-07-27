ls=[4,5,2,3,6,3,1]
target=9
def sum(ls,n=9):
    tr=[]
    l=len(ls)
    for i in range(0,l):
        for j in range(i+1):
            if(ls[i]+ls[j]==n):
                tr.append((ls[i],ls[j]))
    print(set(tr))
sum(ls)


    
# for i in range(len(ls)):
#     for j in range(len(ls)-i-1):
#         if(ls[j]>ls[j+1]):
#             ls[j],ls[j+1]=ls[j+1],ls[j]
# print(ls)

