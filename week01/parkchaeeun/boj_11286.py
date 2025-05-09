import heapq

n = int(input())
heap = []
heapq.heapify(heap)

for i in range(n):
    a = int(input())
    if a != 0:
        # 힙에 (절대값, 실제값) 튜플형식으로 넣기, 절대값 비교 후 실제값 비교
        heapq.heappush(heap,(abs(a),a)) 
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1]) #실제값으로 꺼내기기

