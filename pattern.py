#normal tiangle

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(' ',end=" ")
#     for j in range(i+1):
#         print('$',end=" ")
#     for j in range(i):
#         print('$',end=" ")
#     print()



n=5
for i in range(n):
    for j in range(i+1-1):
        print(' ',end=" ")
    for j in range(n-i):
        print('p',end=" ")
    for j in range(n-i-1):
        print('p',end=" ")
    print()