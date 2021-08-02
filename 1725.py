n = int(input())
fence = []
for i in range(n):
  fence.append(int(input()))

def solve(left, right):
  if left == right:
    return fence[left]

  mid = (left + right) // 2

  ret = max(solve(left, mid), solve(mid+1, right))

  lo = mid
  hi = mid + 1
  height = min(fence[lo], fence[hi])

  ret = max(ret, height * 2)

  while left < lo or hi < right:
    if hi < right and (lo == left or fence[lo-1] < fence[hi+1]):
      hi += 1
      height = min(height, fence[hi])
    else:
      lo -= 1
      height = min(height, fence[lo])

    ret = max(ret, height * (hi - lo + 1))

  return ret

print(solve(0, n-1))
