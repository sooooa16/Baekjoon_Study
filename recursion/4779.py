import sys

def divide(start, end):
    chunk = (end-start) // 3

    if (end-start) == 1:
        return

    for i in range(start + chunk, start + chunk * 2):
        result[i] = ' '

    divide(start, start + chunk)
    divide(start + chunk * 2, end)
    
    return

try:
    while True:
        n = int(sys.stdin.readline().strip())
        result = ['-' for _ in range(3**n)]
        divide(0, 3**n)
        print(''.join(result))
except:
    pass
