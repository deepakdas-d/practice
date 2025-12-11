nums =[3,30,34,5,9]

def largest_number(nums):
    temp=[]
    for i in nums:
        if i>10:
            temp.append(i%10)
            temp.append(i//10)
        if i <10:
            temp.append(i)
    sorted_num=sorted(temp)
    sorted_num.reverse()
    largenum="".join(map(str,sorted_num))
    return largenum
print(largest_number(nums))