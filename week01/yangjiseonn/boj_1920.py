n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
l = list(map(int, input().split()))

for i in l:
    left = 0
    right = n - 1
    find = False

    while left <= right:
        mid = (left + right) // 2
        
        if i > arr[mid]: left = mid + 1
        elif i < arr[mid]: right = mid - 1
        elif i == arr[mid]: 
            print(1)
            find = True
            break
        
    if find == False:
        print(0)
