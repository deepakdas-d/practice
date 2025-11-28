# arr = [5, 1, 5, 20, 5,1]
arr=[1,2,3,4,5]
# Print the third element
# print(len(arr))
# print(arr[1])
# arr[2] = 18
# print(arr)
# arr.append(30)
print(arr)
#
#
#
#
#######################################################
#######################################################
#######################################################
#insert at gven position:
def insert_at_pos(arr,pos,value):
    temp=arr
    counter=0
    while counter<pos-1:
        counter+=1
    temp[counter]=value
    return arr

# print(insert_at_pos(arr,3,18))

# delete an element from specified position
def delete_an_element(arr,value_):
    temp=arr
    if temp is []:
        print("Array is empty")
        return
    for i in range(len(temp)):
  
        if temp[i]==value_:
            del temp[i]
            break
    return arr

# print(delete_an_element(arr,20))

# find index of an element
def index_of_element(arr,value):
    arr
    for i in range(len(arr)):
        if arr[i]==value:
            return i
# print("the index of the value is ", index_of_element(arr,5))

#sum of elements in a array
def sum_of_elements(arr):
    arr
    counter=0
    sum=0
    while counter<len(arr):
        sum+=arr[counter]
        counter+=1
    return sum
# print("the sum of elements in array is ",sum_of_elements(arr))

def max_and_min(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i > max:
            max=i
        if i<min:
            min=i
    return max,min
# print("the max value is:",max_and_min(arr))      

#reverse a array in place
def reverse_in_place(arr):
        left=0
        right=len(arr)-1
        while left<right:
            temp=arr[left]
            arr[left]=arr[right]
            left+=1
            arr[right]=temp
            right-=1
        return arr
# print(reverse_in_place(arr))

def binary_search(arr,val):
    target=val
    mid=len(arr)//2
    first=arr[0]
    last=arr[len(arr)-1]

    if target == arr[mid]:
        return mid
    elif target<arr[mid]:
        # search left
        last=mid
        for i in range(last):
            if arr[i] == target:
                return i

    elif target>mid:
        # search right
        first=mid
        for i in range(first,len(arr)):
            if arr[i]==target:
                return i

        

print(binary_search(arr,5))
print(binary_search(arr,3))


    





