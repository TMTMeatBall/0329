dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # result = 1
    q = [(x, y)]
    while q:
        ey, ex = q.pop()
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 'L' and check[nx][ny] == False:
                    # result += 1
                    check[nx][ny] = True
                    q.append((nx, ny))
    return

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    cnt = 0
    max_v = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L' and check[i][j] == False:
                check[i][j] = True
                cnt += 1
                max_v = max(max_v,bfs(i,j))