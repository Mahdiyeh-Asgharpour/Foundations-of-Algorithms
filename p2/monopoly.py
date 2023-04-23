x=input()
array=x.split(",")
#index
y=0
#next move
z=0
#moves
n=0
na=[]
z=int(array[y])+int(y)
def f(z,y):
    if int(array[y])==0:
        n=n+1
        na.append(array[y])
        print("Unreachable!")
    else:
        if z>len(array):
            pass
        else:
            y=y+1
            z=int(array[y])+int(y)
            n=n+1
            na.append(array(y))
            f(z,y)
        print(n)
f(z,y)
print(na)