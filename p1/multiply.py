# we should get 2 numbers
n1=input("number 1:")
n2=input("number 2:")
# we have 3 array , carry , charat n1 and n2
# it means we use charat() for numbers
array1=[]
array2=[]
carry=[]
answer=[]
#at first all of element in carry is 0 
if(n1.__len__()>=n2.__len__()):
    for i in range(n1.__len__()):
        carry.append(0)
else:
    for i in range(n2.__len__()):
        carry.append(0)
for i in range(n1.__len__()):
    array1.append(n1[i])
for i in range(n2.__len__()):
    array2.append(n2[i])
def Multiply(n):
    while(n>=0):
    #answer multiply
        multi==array1[n]*array2[n]
        if(multi>9):
            carry.insert(n+1, multi/10)
        if(n1.__len__()>=n2.__len__()):
            if(n==0 or n==n1.__len__()):
                answer.append(multi+int(carry[n]))
        else:
            if(n==0 or n==n2.__len__()):
                answer.append(multi+int(carry[n]))
        multiply(n-1)
if(n1.__len__()>=n2.__len__()):
    Multiply(n1.__len__())
else:
    Multiply(n2.__len__())
