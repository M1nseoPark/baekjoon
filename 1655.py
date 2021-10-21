import heapq
import sys

# 1. maxHeap의 크기는 minHeap의 크기와 같거나 1 더 크다
# 2. maxHeap의 최대 원소는 minHeap의 최소 원소보다 작거나 같다        
n = int(sys.stdin.readline())
minHeap = []
maxHeap = []
for i in range(n):
    x = int(sys.stdin.readline())
    
    # 우선 1번 식부터 만족시킴
    if len(minHeap) == len(maxHeap):
        x *= -1
        heapq.heappush(maxHeap, x)
    else:
        heapq.heappush(minHeap, x)
    
    # 2번 불변식이 깨졌을 경우 복구함
    if len(minHeap) != 0 and len(maxHeap) != 0 and minHeap[0] < (maxHeap[0] * -1):
        a = maxHeap[0] * -1
        b = minHeap[0] * -1
        heapq.heappop(maxHeap)
        heapq.heappop(minHeap)
        heapq.heappush(maxHeap, b)
        heapq.heappush(minHeap, a)

    print(maxHeap[0] * -1)   # 수열의 중간값은 항상 maxHeap의 루트에 있게 됨
