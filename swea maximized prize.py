def permute(cnt):
    global result


    if cnt == M:
        result = max(result,int(''.join(N)))
        return #기저조건

    for i in range(len(N)-1):
        for j in range(i+1,len(N)):

            N[i],N[j] = N[j],N[i] #자리 바꾸고

            permute(cnt+1) #횟수 1 더해주고

            N[i],N[j] = N[j],N[i] #다시 자리를 원래대로


T = int(input())
for tc in range(1,T+1):
    N, M = input().split()
    N = list(N)
    M = int(M)

    if M > len(N):
        if (M-len(N)) % 2 == 1:
            M = len(N) -1
        else:
            M = len(N)

    result = 0

    permute(0)

    print(f'#{tc} {result}')