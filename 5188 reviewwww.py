dx = [1, 0]  # 하
dy = [0, 1]  # 우


def solution(x, y, sum):
    global min_sum

    if min_sum <= sum:
        return
    # pruning
    if x == N - 1 and y == N - 1:
        if min_sum > sum:
            min_sum = sum
        return
    # 기저조건

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            solution(nx, ny, sum + arr[nx][ny])


# 우하탐색하고 array안에 존재가능하면 nx,ny로 진행하고, sum = sum + arr[nx][ny] 로 계속 더하는 것을 재귀호출함


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10001

    solution(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')
