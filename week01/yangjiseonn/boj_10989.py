import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001 # 숫자 범위 1~10000

for i in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):   # count[0]은 제외하고 1부터 10000까지
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)