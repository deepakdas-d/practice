# l=[1,'b',False,2,True,'a',3,'4',True]
# s=0
# n=0
# for i in l:
#     if isinstance(i,int):
#         n+=1
        
# else:
#     s+=1

# print('num',n)
# print('str',s)

num = 29  # Number to check
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number, divisible by {i}.")
        break
else:
    print(f"{num} is a prime number.")
