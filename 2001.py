T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M, N = map(int, input().split())                                   
    sq_list = []

    for i in range(M):
        a = list(map(int, input().split()))                          
        sq_list.append(a)                             

    max_sq = 0
    max_list = []
    for i in range(M-N+1):
        for j in range(M-N+1):
            max_sq = 0
            for k in range(N):
                for l in range(N):
                    max_sq += sq_list[i+k][j+l]                                       
            max_list.append(max_sq)
    
    print(f'#{test_case} {max(max_list)}')