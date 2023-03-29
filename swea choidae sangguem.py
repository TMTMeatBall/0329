# 재귀 또는 DFS를 사용하기
# money (int)32888
# -> ['3','2','8','8','8']
def dfs(money, count):
    '''
    money 상금
    count 교환수
    '''
    # 종료조건
    if count == 0:
        existed[count].add(int(''.join(money)))
        return
    # 가지치기
    if int(''.join(money)) in existed[count]:
        return
    existed[count].add(int(''.join(money)))
    for i in range(len(money)):
        for j in range(i + 1, len(money)):
            money[i], money[j] = money[j], money[i]
            dfs(money, count - 1)
            money[i], money[j] = money[j], money[i]


T = int(input())
for tc in range(1, T + 1):
    # 상금,교환횟수
    money, count = map(int, input().split())
    result = []
    existed = [set() for _ in range(count + 1)]
    dfs(list(str(money)), count)

    print(f'#{tc} {max(existed[0])}')
