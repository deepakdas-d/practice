#file Handling


with open('sample.txt','r')as f:
    read=f.read()
    print(read)

# C=read.replace('i','$')
# c= read.replace('I','$')
c=''
for i in read:
    if i=='I':
        c+='$'
    else:
        c+=i

with open('sample.txt','w') as f:
    f.write(c)
   
with open('sample.txt','r')as f:
    read=f.read()

with open('copy.txt','w')as f:
      f.write(read)

