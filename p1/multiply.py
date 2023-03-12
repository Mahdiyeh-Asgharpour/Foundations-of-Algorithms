# we should get 2 numbers
n1=input("number 1:")
n2=input("number 2:")
# we have 3 array , carry , charat n1 and n2
# it means we use charat() for numbers
array1=[]
array2=[]
carry=[]
#at first all of element in carry is 0 
if(n1.__len__()>=n2.__len__()):
    for i in range(n1.__len__()):
        carry.append(0)
else:
    for i in range(n2.__len__()):
        carry.append(0)
for i in range(n1.__len__()):
    array1.append(n1)
for i in range(n2.__len__()):
    array2.append(n2)

