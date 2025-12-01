num=[0,0,1,1,1,2,2,3,3,4]
def remove_dupolicate(num):
    s=set()
    res=[]
    for i in num:
            if i not in s:      
             s.add(i) 
             res.append(i)
    return res
print(remove_dupolicate(num))
                 




