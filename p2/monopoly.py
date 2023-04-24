x=input()
arr=x.split(",")
# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns minimum number of jumps
# to reach arr[h] from arr[l]
 
 
def minJumps(arr, l, h):
 
    # Base case: when source and
    # destination are same
    if (h == l):
        return 0
 
    # when nothing is reachable
    # from the given source
    if (int(arr[l]) == 0):
        return float('inf')
 
    # Traverse through all the points
    # reachable from arr[l]. Recursively
    # get the minimum number of jumps
    # needed to reach arr[h] from
    # these reachable points.
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + int(arr[l]) + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1
 
    return min
 
 
# Driver program to test above function
n = len(arr)
if  minJumps(arr, 0, n-1)==float('inf'):
    print("Unreachable!")
else:
    print( minJumps(arr, 0, n-1))
 
# This code is contributed by Soumen Ghosh