import sys

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heap.append(x)
        idx = len(heap) - 1
        while idx > 0 and heap[(idx-1)//2] > heap[idx]:
            heap[idx], heap[(idx-1)//2] = heap[(idx-1)//2], heap[idx]
            idx = (idx - 1) // 2
    else:
        if len(heap) == 0:
            print('0')
        else:
            print(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            here = 0
            while True:
                left = here * 2 + 1
                right = here * 2 + 2
                if left >= len(heap):
                    break
                nextt = here
                if heap[nextt] > heap[left]:
                    nextt = left
                if right < len(heap) and heap[nextt] > heap[right]:
                    nextt = right
                if nextt == here:
                    break
                heap[here], heap[nextt] = heap[nextt], heap[here] 
                here = nextt
