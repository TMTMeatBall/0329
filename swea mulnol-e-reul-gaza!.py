dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid(x, y):
    return -1 < x < N and -1 < y < M


def solution(x, y, now_sum):
    global min_sum

    if (x, y) == (N - 1, M - 1):
        min_sum = min(min_sum,now_sum)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if is_valid(nx,ny):
            solution(nx,ny,now_sum + 1)



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # 격자 밖으로 나가면 안됨
    # 물인 칸으로 이동하기 위한 최소 횟수와 모든 이동횟수의 합을 출력하기.
    # 물을 출발지점으로 잡고 사방탐색 하면서 땅으로 가는 모든 횟수를 센다
    visited =[[0]*M for _ in range(N)]


    for i in range(N):  # col
        for j in range(M):  # row
            if arr[i][j] == 'W':
                x = i
                y = j
                # 물의 위치 잡기

    solution(x, y, min_sum)

    print(f'#{tc} {min_sum}')
