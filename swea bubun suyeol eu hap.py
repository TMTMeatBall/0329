# def frac(i, j):
#     if i == j:
#         sum = 0
#         cnt = 0
#         for i in range(N):
#             if bin[i] == 1:
#                 sum += A[i]
#         if sum == K:
#             for i in range(N):
#                 cnt += 1
#
#             return print(cnt)
#     else:
#         bin[i] = 0
#         frac(i + 1, j)
#         bin[i] = 1
#         frac(i + 1, j)
#
#
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N, K = map(int, input().split())
# #     A = list(map(int, input().split()))
# #     bin = [0] * N
# #
# A = [1,2,1,2]
# N = len(A)
# K = 3
# bin = [0] * N
# frac(0, K)

# N = a리스트 요소의 갯수, k는 a의 부분 수열의 합이 k가 되는 경우의 수를 정답에 출력함
#부분집합 뽑는 로직 쓰고, 그 부분집합의 총합이 K인 경우만을 받음
def frac(i,k):
    if i == k: #기저조건
        sum = 0
        cnt = 0
        for i in range(N):
            if bit[i] == 1:
                cnt += 1
                sum += A[i]

        if sum == K:
            for i in range(N):
                if bit[i] == 1:
                    print(A[i],end=' ')
            print(cnt)
    else:
        bit[i] = 0
        frac(i+1,k)
        bit[i] = 1
        frac(i+1,k)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    N = len(A)
    bit = [0] * N
