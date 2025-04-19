# 1 2 3 
# 6 5 4
# 7 8 9
# 12 11 10

c=0
for i in range(1,5):
    row=[]
    for j in range(1,4):
        c+=1
        row.append(c)
    if i%2==0:
        row.reverse()
    for num in row:
        print(num,end=" ")
    print()


       


