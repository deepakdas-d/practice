gas=[2,3,4]
tank=[3,4,3]
def greedy(gas,tank):
        net=0
        start=0
        if len(gas)==len(tank) and sum(gas)>=sum(tank):
            for i in range(start,len(gas)):
                    net+= gas[i]-tank[i]
                    if net<0:
                        net=0    
                        start=i+1
        else: 
              return -1
        return start
print(greedy(gas,tank))

