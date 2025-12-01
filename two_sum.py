nums = [2, 7, 11, 15]
target = 9

def twosum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(length-1, i, -1): 
            if nums[i] + nums[j] == target:
                return [i, j]

    return "not found"  


output= twosum(nums,target)
print(output)