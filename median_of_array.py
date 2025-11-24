arr=[1,2]
arr2=[3,4]

arr+=arr2
arr.sort()
print(arr)
n=len(arr)
if n%2!=0:
    median=arr[n//2]
else:
    median=arr[n//2]+arr[n//2-1]
    median/=2.0
print(median)