# we should get 2 numbers
n1=input("number 1:")
n2=input("number 2:")
#this function is in internet
def karatsuba(m,n):
    if(int(m)<10 or int(n)<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)

        k = max(len(mstring), len(nstring))
        mid=int(k/2)
            #finding a and c i.e. the higher bits for each number
        a = int(mstring[:-mid])
        c = int(nstring[:-mid])

            #finding b and d i.e. the lower bits for each number
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])

            #finding ac, bd and ad_plus_bc
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd
#call function
karatsuba(n1,n2)
#conditions is in document, we use[] for string , so we change it , then we want do conditions so we change it to int.
print(int(str(karatsuba(n1,n2))[0])**int(str(karatsuba(n1,n2))[len(str(karatsuba(n1,n2)))-1]))