l = list(map(int,input().split()))

while(sorted(l)!=l):
    for i in range(4):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            print(*l)

