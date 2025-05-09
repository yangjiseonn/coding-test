n = int(input())
count = 0
arr = []

def sum(inputs):
    count = 0
    for i in inputs:
        if i.isdigit():
            count += int(i)
    return count

for i in range(n):
    k = input()
    arr.append(k)

arr.sort(key=lambda x: (len(x), sum(x), x))

for i in arr:
    print(i)