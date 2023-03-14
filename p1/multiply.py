# we should get 2 numbers
n1=input("number 1:")
n2=input("number 2:")
# we have 1 array  carry ,it does if answer multiply >9 we should do  answer multiply /10 and save to carry
carry=[]
answer=[]
#at first all of element in carry is 0 
if(n1.__len__()>=n2.__len__()):
    for i in range(n1.__len__()):
        carry.append(0)
        answer.append(0)

else:
    for i in range(n2.__len__()):
        carry.append(0)
        answer.append(0)

def Multiply(n):
    if(n<0):
        return
    else:
    #answer multiply
        multi=int(n1[n])*int(n2[n])
        if(multi>9):
            carry[n-1]=int(multi/10)
        answer[n]=int(multi%10)+int(carry[n])
        Multiply(n-1)
#call function
if(n1.__len__()>=n2.__len__()):
    Multiply(len(n1)-1)
else:
    Multiply(len(n2)-1)
print(answer,carry)