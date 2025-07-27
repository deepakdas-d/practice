num=[1,2,3,4,4,2,3,1]

freq={}

for n in num:
    freq[n]=freq.get(n,0)+1
print(freq)