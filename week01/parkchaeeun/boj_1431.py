n = int(input())
l = list()
for _ in range(n):
    l.append(input())

def digit_sum(s): # 숫자 합을 구하는 함수수
    return sum(int(c) for c in s if c.isdigit())

l.sort(key = lambda x: (len(x),digit_sum(x), x))

print(*l)



