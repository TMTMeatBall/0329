#3개씩 8조 4번 가벼운 조 1개에서 2개 뽑아 서로 비교 1번 총 5번
# 분할 정렬 - 시간복잡도 감소를 위해 요구됨 (nlogn)
# 병합 정렬(merge sort)
# 일단 전부 쪼갠 뒤에, 2개짜리로 묶으면서 정렬,
# 2개짜리를 묶어서 4개짜리로 정렬, 이하 반복.
# def merge_sort(list_m):
#     if length(list_m) == 1:
#         return m
#     list_a = []
#     list_b = []
#     for i in range(len(list_m // 2)):
#         list_a.append(list_m[i])
#     list_b.append(list_m[len(list_m // 2):])
#
#     for i in range(len(list_a)):
#         for j in range(i + 1, len(list_a)):
#             if list_a[]

#분할정복 기법을 사용한 정렬 알고리즘
# 병합과정
# def merge(left, right):
#     list result
#
# while length(left) > 0 or length(right) > 0:
#     if length(left) > 0 and length(right) > 0:
#
# 예시코드
# def msort(m):
#     if len(m) == 1:
#         return m
#     middle = len(m) // 2
#     left = m[0:middle + 1]
#     right = m[middle:]
#
#     # for x in range(m[0:middle+1]):
#     #     left.append(m[x])
#     # for x in range(m[middle:]):
#     #     right.append(m[x])
#
#     left = msort(left)
#     right = msort(right)
#     return merge(left, right)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     msort(arr)


# 다른 방식
# def msort(s, e):  # 시작인덱스와 끝 인덱스를 변수로 갖는 함수 msort
#     if s == e:
#         return
#     m = (s + e) // 2
#     msort(s, m)
#     msort(m + 1, e)
#     l, r = s, m + 1  # 왼쪽,오른쪽
#     while l <= m or r <= e:
#         if l <= m and r <= e:
#             if arr[l] <= arr[r]:
#                 tmp[k] == arr[l]
#                 l += 1
#             else:
#                 tmp[k] = arr[r]
#                 r += 1
#             k += 1
#         elif l <= m:
#             while l <= m:
#                 tmp[k] = arr[l]
#                 l += 1
#                 k += 1
#
#     k = 0
#     while i < k:
#         arr[s + i] = tmp[i]
#     return
#
#
# # tmp에 정렬 결과를 저장한다.
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     tmp = [0] * N
#     msort(0, N)
#
#
# # 퀵 정렬
# # 병합정렬과 같이 분할정복 기법의 하나
# 병합은 단순 2분할의 반복
# 퀵 정렬은  pivot 중심으로 작은 것은 왼쪽, 큰 것은 오른쪽에 두는 방식의 정렬
#  partitioning 함수를 따로 작성하는 것으로 pivot을 설정하고,
#  그 pivot을 기준으로 좌우로 정렬하는 것을 재귀적으로 호출하는 게 원리
# def quicksort(A[], l, r):
#     if l < r:
#         s < - partition(a, l, r)  # 여러 가지 파티션의 방식이 있다.
#         quicksort(A[], l, s - 1)
#         quicksort(A[], s + 1, r)
# 피봇이 너무 작거나, 너무 큰 경우에는 복잡도가 크게 증가 최대 o=n^2
#
# # hoare-partition
# # 피봇 값을 구하는 방식들
# # 맨 왼쪽/오른쪽/중간값(3개의 무작위 값을 받아서 중간값으로 해결)
# partition(A[], l, r)
#
# while i <= j 커지는 i가 작아지는 j보다 커진 순간 종료됨
#     while i <= j and A[i] <= p: i + +
#     while i <= j and A[j] >= p: j - -
#     if i < j: swap(A[i], A[j])
#i는 오른쪽으로 진행하다가 자신보다 큰 값이 나오면 거기서 스톱
#j는 왼쪽으로 진행하다가 피봇보다 작은 값이 나오면 피봇과 교환
# # lomuto-partition
# 피봇과 값이 같은 경우에도 스왑이 일어나는 단점이 존재
# 하지만 간단한 구조
# def partition(A[], p, r):
# x < - A[r]
# i < - p - 1
# for j in p -> r-1
# if A[j] <= x
#     if A[j] <= x
#         i + +, swap(A[i], A[j])
# swap(A[i + 1], A[r])
# return i + 1


# ??????
# def hoare(A,l,r):
#     pivot = A[l] #가장 좌측 원소 기준
#     i=l #피봇보다 큰 값을 찾으면서 오른쪽으로
#     j=r #피봇보다 작은 값을 찾아므녀서 왼쪽으로
#     while i<=j: #두개가 겹치지 않은 상태
#         while i<=j and A[i] <= pivot:
#             i += 1
#         while i<=j and A[j] >= pivot:
#             j -= 1
#         if i < j: #교차하지 않은 경우
#             A[i],A[j] = A[j], A[i]
#     A[j],A[l] = A[l],A[j]
#     return j
#
# def qsort(A, l, r):
#     global cnt
#     cnt += 1
#     if l < r:
#         s = hoare(A, l, r)
#         qsort(A, l, s - 1)
#         qsort(A, s + 1, r)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     qsort(arr, 0, N - 1)
#     # print(*arr,cnt)
#     # print(arr[500000])
#     print(arr[500000])
#     print(cnt)
