def cout(a,b,cin=0):
    return ((a^b) and cin) or (a and b)
def fsum(a,b,cin=0):
    return (a ^ b)^cin
def adder(a,b):
    a = a[::-1]
    b = b[::-1]
    final=[]
    for i in range(len(a)):
        if i==1:
            final.append(fsum(a[i],b[i]))
        else:
            final.append(fsum(a[i],b[i],cout(a[i-1],b[i-1])))
        i+=1
    return final[::-1]
