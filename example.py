#python
s='deepakdas'
vowels=['a','e','i','o','u']
v=0
c=0
for i in s:
    for j in vowels:
        if i in j:
            v+=1
            break
    else:
        c+=1

print(c)
print(v)



# v=0
# c=0
# for i in s:
#     if i in vowels:
#         v+=1
#     else:
#         c+=1
# print(v)
# print(c)
 