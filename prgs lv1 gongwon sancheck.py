def solution(park, routes):
    h = len(park)
    w = len(park[0])
    x = 0
    y = 0

    nav = {
        'S': [1, 0],
        'N': [-1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }
    # 동서남북 받기
    # 1.시작점 S의 위치 받기
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j
    for route in routes:
        direction, distance = route.split()  # 각 경우를 split하기 때문에 받을 수 있음
        distance = int(distance)
        flag = 0
        nx = x
        ny = y
        for i in range(1, distance + 1): #distance는 그 거리 그대로 해야 하므로 인덱싱에서 1,distance+1해야 한다
            nx += nav[direction][0] #딕셔너리 nav에서 끄집어내서 nx,ny 반환하는 방법
            ny += nav[direction][1]

            if nx >= h or nx < 0 or ny >= w or ny < 0 or park[nx][ny] == 'X':
                # 이동 중에 장애물이 있다면. i 가 distance까지 계속 더해가므로 중간에 장애물 만나면 flag에 반영해서 불가능한 행동으로 break할 수 있다.
                flag = 1
                break

        if flag == 0:
            x += nav[direction][0] * distance
            y += nav[direction][1] * distance
    answer = [x,y]
    return answer


# s = 시작지점, o = 통로, x = 장애물
# 장애물을 만나거나 공원을 벗어나지 않는다면 명령을 실행
# E/W/S/N + 임의의 숫자로 이동방향,거리를 정함
# 2차원배열을 받는다/시작점 s를 받는다/
# 동서남북을 받아서 움직이게 해보기
