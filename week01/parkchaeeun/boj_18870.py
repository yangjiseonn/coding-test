# ### 시간초과로 오류
# import sys
# input = sys.stdin.readline
# n = int(input())
# x = list(map(int, input().split()))

# x_ = sorted(x)
# l = []
# for i in x:
#     l.append(x_.index(i)) 
#     # .index(i)는 i가 처음 등장하는 인덱스를 찾기 위해 왼쪽부터 순차 탐색 + for문-> O(N^2)
# print(*l)

### 딕셔너리로 인덱스 매핑하여 해결 -> 딕셔너리는 해시테이블을 사용해서 O(1)로 접근 가능
import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))

x_ = sorted(set(x)) # 서로 다른 좌표 개수를 구해야함으로 집합으로 중복 제거 -> O(N log N)
                    # 중복제거는 -> O(N), sorted() -> O(N log N)
dic = {val: idx for idx, val in enumerate(x_)}
l = [dic[i] for i in x]
print(*l)