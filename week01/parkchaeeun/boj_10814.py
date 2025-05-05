import sys

input = sys.stdin.readline
output = sys.stdout.write
n = int(input())
l = [input().split() for _ in range(n)]
l.sort(key = lambda x: int(x[0]))

for i in l:
    output(i[0]+" "+i[1]+"\n")