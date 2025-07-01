def recursion(start, end):
    count = 0
    while start <= end:
        if arr[start] == '(':
            pair = 1
            tmp = start
            count -= 1
            while True:
                if pair == 0:
                    break
                start += 1
                if arr[start] == '(':
                    pair += 1
                elif arr[start] == ')':
                    pair -= 1
            count += int(arr[tmp-1])*recursion(tmp+1, start-1)
        elif arr[start] == ')':
            start += 1
        else:
            start += 1
            count += 1
    return count               
    
arr = list(str(input()))

print(recursion(0, len(arr)-1))