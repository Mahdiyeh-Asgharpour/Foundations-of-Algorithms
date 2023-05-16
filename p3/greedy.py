x=input()
y=input()
xx=x.split()
yy=y.split()

 
# Returns min number of squares needed
def minimumSquare(a, b):
 
    result = 0
    rem = 0
 
    # swap if a is small size side .
    if (a < b):
        a, b = b, a
 
    # Iterate until small size side is
    # greater than 0
    while (b > 0):
     
        # Update result
        result += int(a / b)
 
        rem = int(a % b)
        a = b
        b = rem
 
    return result
 

print(minimumSquare(int(xx[0]), int(yy[0])))
 
