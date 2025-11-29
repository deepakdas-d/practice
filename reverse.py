
def reverse_int(num):
    num=abs(num)
    reversed_num=0
    while num>0:
        dec=num%10
        reversed_num=reversed_num*10+dec
        num=num//10
    if num>2**31-1 or num<-2**31:
        return 0
    if num <0:
        return -reversed_num
    else:
        return reversed_num
print(reverse_int(-96497611 ))