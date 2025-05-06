import sys

input = sys.stdin.readline
count = [0] * (10000+1)

n = int(input())
for _ in range(n):
    a = int(input())
    count[a] += 1
    
for i in range(len(count)):
    for _ in range(count[i]):
        print(i)


