string="deepak"
string2=""
# print(string[::-1])
length=len(string)
for i in range(length-1,-1,-1 ):
    string2+=string[i]
    # print(string[i],end=" ")
# print(string2)
if string==string2:
    print("palindrome")
else:
    print("not a palindrome")
