import heapq
import sys

n = int(sys.stdin.readline())
heap = []
mheap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        if x > 0:
            heapq.heappush(heap, x)
        else:
            x *= -1
            heapq.heappush(mheap, x)
    else:
        if len(heap) == 0 and len(mheap) == 0:
            print('0')
        elif len(heap) == 0:
            print(heapq.heappop(mheap) * -1)
        elif len(mheap) == 0:
            print(heapq.heappop(heap))
        else:
            pmin = heap[0]
            mmin = mheap[0]
            if pmin < mmin:
                print(heapq.heappop(heap))
            else:
                print(heapq.heappop(mheap) * -1)
