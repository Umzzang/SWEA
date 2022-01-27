T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle_list = []
    for i in range(N):
        puzzle_list += [list(map(int, input().split()))]

    print(puzzle_list)
    count = 0
    for i in range(N):
        for j in range(N):
        
            if puzzle_list[i][j] == 0 and 0 not in puzzle_list[i][j+1:j+K+1] :
                try :
                    if puzzle_list[i][j+K+2] == 0:
                        count += 1
                except:
                    count += 1
    # for j in range(N):
    #     for i in range(N-K):
    #         if 0 not in puzzle_list[i:K][j] :
    #             count += 1
                
    print(count)