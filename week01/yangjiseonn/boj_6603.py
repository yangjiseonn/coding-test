# dfs
def dfs(s, depth):
    if depth == 6:
        print(*comb, sep=" ")
        return

    for i in range(s, len(arr)):
        comb[depth] = arr[i]
        dfs(i+1, depth+1)


while(1):
    arr = list(map(int, input().split()))
    n = arr.pop(0)

    if n == 0: break

    comb = [0]*6
    dfs(0, 0)
    print()