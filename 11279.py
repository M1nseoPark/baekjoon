import sys

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    # x가 0이 아니라면 배열에 값 추가
    if x != 0:
        heap.append(x)   # 먼저 힙의 맨 끝에 새 원소 추가
        idx = len(heap) - 1
        # 루트에 도달하거나 새 원소가 더 크거나 같은 부모 노드를 만날 때까지 반복함
        while idx > 0 and heap[(idx-1)//2] < heap[idx]:    
            heap[idx], heap[(idx-1)//2] = heap[(idx-1)//2], heap[idx]
            idx = (idx - 1) // 2
    # x가 0이라면 배열에서 가장 큰 원소를 출력하고 그 값을 배열에서 제거함
    else:
        if len(heap) == 0:   # 힙이 비어있다면 0을 출력함
            print('0')
        else:
            print(heap[0])   # 힙에서 가장 큰 원소는 항상 트리의 루트임
            heap[0] = heap[-1]   # 힙의 마지막 노드를 루트에 덮어 씌움
            heap.pop()   # 마지막 노드를 제거함
            here = 0
            while True:
                left = here * 2 + 1   # 왼쪽 자식 노드
                right = here * 2 + 2   # 오른쪽 자식 노드
                if left >= len(heap):  # 트리의 바닥에 도달한 경우 중단
                    break 
                # 두 자식 노드가 가진 원소 중 더 큰 원소를 선택해 루트가 갖고 있는 원소와 맞바꿈
                nextt = here
                if heap[nextt] < heap[left]:
                    nextt = left
                if right < len(heap) and heap[nextt] < heap[right]:
                    nextt = right
                if nextt == here:   # 두 자손이 모두 자신 이하의 원소를 갖고 있을 때 중단
                    break
                heap[here], heap[nextt] = heap[nextt], heap[here] 
                here = nextt
