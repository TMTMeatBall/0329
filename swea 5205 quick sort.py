def partition(A, l, r):
    # s = mid[1]
    s = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= s:
            i += 1
        while i <= j and A[j] >= s:
            j -= 1
        if i < j:
            A[j], A[i] = A[i], A[j]
    A[j], A[l] = A[l], A[j]
    return j


def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    mid = []
    mid.append(A[0])
    mid.append(A[-1])
    mid.append(A[N // 2 - 1])
    mid.sort()
    # print(mid)
    if A[0] != mid[1] and mid[1] == A[-1]:
        A[0], A[-1] = A[-1], A[0]
    elif A[0] != mid[1] and mid[1] == A[N // 2 -1]:
        A[0], A[N // 2 -1] = A[N // 2 -1], A[0]

    # print(A)

    qsort(A, 0, N-1)

    # print(A)

    # if len(A) % 2:
    print(f'#{tc} {A[N // 2]}')
    # else:
    #     print(f'#{tc} {A[N // 2 - 1]}')
#중간값으로 한 풀이
#