x=input()
arr=x.split(",")
def monopoly(arr, n):
    path = [[] for i in range(n)]

    path[n - 1].append(n - 1)

    for i in range(n - 2, -1, -1):
        if int(arr[i]) >= n - i - 1:
            path[i].append(i)
            path[i].append(n - 1)
        else:
            min_jumps = float('inf')
            index = 0
            for j in range(i + 1, n - 1):
                if j - i <= int(arr[i]):
                    if len(path[j]) <= min_jumps:
                        min_jumps = len(path[j])
                        index = j

            path[i].append(i)
            path[i].extend(path[index])

    if path[0][len(path[0]) - 1] == n - 1:
        print(len(path[0]) - 1)
        print(*[arr[i] for i in path[0]], sep="-")
    else:
        print("Unreachable!")
        print(*[arr[i] for i in path[0]], sep="-")



n = len(arr)
monopoly(arr, n)
