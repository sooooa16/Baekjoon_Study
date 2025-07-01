n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0

def cut(start_x, start_y, end_x, end_y):
    global white, blue
    temp = graph[start_x][start_y]
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if temp != graph[x][y]:
                cut(start_x, start_y, end_x//2, end_y//2)
                cut(end_x//2, start_y, end_x, end_y) 
                cut(start_x, end_y//2, end_x//2, end_y)
                cut(end_x//2, end_y//2, end_x, end_y)
    
    if graph[start_x][start_y] == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, n, n)
print(white)
print(blue)