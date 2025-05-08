n = int(input())
arr = list(map(int, input().split()))  # 2 4 -10 4 -9
l = sorted(set(arr))  # -10 -9 2 4

dic = {l[i]: i for i in range(len(l))}  # l[i]를 원소로 하고 그 인덱스 i를 값으로 하는 딕셔너리 생성
# {-10:  0, -9: 1, 2: 2, 4: 3}

# dic = {}
# for i in range(len(l)):
#     dic[l[i]] = i

for i in arr:
    print(dic[i], sep=" ")  # dic[i]는 i가 l 리스트에서 몇 번째로 위치하는지 나타냄