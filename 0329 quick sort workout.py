# 배열 데이터를 퀵 정렬하는 함수를 작성
# 11,45,23,81,28,34
# 11,45,22,81,23,34,99,22,17,8
# 1,1,1,1,1,0,0,0,0,0

def partition(A, l, r):
    s = A[l]  # 배열 왼쪽에 있는 값을 피봇으로 설정함
    i = l #0
    j = r #A[-1]
    while i <= j:  # i와 j가 서로 교차하는 순간까지 반복
        while i <= j and A[i] <= s: #왼쪽이 없으면 리스트를 벗어나고, 오른쪽이 없으면 i가 비교하지 않음
            i += 1
        while i <= j and A[j] >= s:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i] #
    A[j], A[l] = A[l], A[j] #i>j인 순간에서 전체 while문이 종료되므로 A[i]>pivot,A[j]<pivot
    #의 상태일 것이므로, 전체 정렬에서 뒤바뀌는 pivot이 좌측에 위치하므로, A[0]<pivot을 만족할 수 있도록
    #그 순간의 A[j]가 만족하기 때문에 j랑 바꾸고 해당 인덱스를 return하는 것으로 i가 가능한 경우는 pivot이
    #우측에 있는 경우여야만 가능할지도? 랜덤으로 해서 중앙값을 한 경우에는?그게 실제 중앙값과의 차이는?
    return j #피봇 위치(인덱스)를 반환함
    #

def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


A = list(map(int, input().split()))
qsort(A, 0, len(A)-1)
print(A)

#신기해