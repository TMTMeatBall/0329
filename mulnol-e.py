dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    dist = [[987654321] * M for _ in range(N)]

    queue = [0] * N * M
    front = -1
    rear = -1

    for i in range(N):  # col
        for j in range(M):  # row
            if arr[i][j] == 'W': # 물의 위치 잡기
                rear += 1
                queue[rear] = (i,j)
                dist[i][j] = 0
    while front != rear:
        front += 1
        x, y = queue[front]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 'L' and dist[nx][ny] == 987654321:
                dist[nx][ny] = dist[x][y] +1
                rear +=1
                queue[rear] = (nx,ny)
    result = 0
    for i in dist:
        for j in i:
            result += j

    print(f'#{tc} {result}')