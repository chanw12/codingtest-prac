from collections import deque


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
rst = 0
check = False

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [[0 for _ in range(m)] for _ in range(n)]
    result =0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result+=bfs(i,j)
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0 :
                graph[i][j] = 0
    if result == 0:
        break
    if result >= 2:
        check = True
        break

    rst += 1

if check:
    print(rst)
else:
    print(0)

            
    

            



