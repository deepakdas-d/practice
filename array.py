arr = [5, 10, 15, 20, 25]
# Print the third element

# print(arr[1])
# arr[2] = 18
# print(arr)
# arr.append(30)
# print(arr)
def insert_at_pos(arr,pos,value):
    temp=arr
    counter=0
    while counter<pos-1:
        counter+=1
    temp[counter]=value
    return arr

print(insert_at_pos(arr,3,18))

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

print(delete_an_element(arr,20))


def index_of_element(arr,value):
    temp=arr
    for i in range(len(temp)):
        if temp[i]==value:
            return i
print(index_of_element(arr,5))

