k = int(input())
arr = list(map(int, input().split()))

def divide(i, start, end):
    if start == end:
        result[i].append(arr[start])
        return
    root = start + (end-start) // 2
    result[i].append(arr[root])
    divide(i+1, start, root-1)
    divide(i+1, root+1, end)

result = list([] for _ in range(k))
divide(0, 0, len(arr)-1)
for i in range(0, k):
    print(*result[i])