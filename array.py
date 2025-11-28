arr = [5, 1, 5, 20, 5,1]
# Print the third element

# print(arr[1])
# arr[2] = 18
# print(arr)
# arr.append(30)
# print(arr)
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

print(insert_at_pos(arr,3,18))

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
    temp=arr
    for i in range(len(temp)):
        if temp[i]==value:
            return i
# print("the index of the value is ", index_of_element(arr,5))

#sum of elements in a array
def sum_of_elements(arr):
    temp=arr
    counter=0
    sum=0
    while counter<len(temp):
        sum+=temp[counter]
        counter+=1
    return sum
# print("the sum of elements in array is ",sum_of_elements(arr))

def max_and_min(arr):
    temp=arr
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i > max:
            max=i
        if i<min:
            min=i
    return max,min
                
      
print("the max value is:",max_and_min(arr))      


