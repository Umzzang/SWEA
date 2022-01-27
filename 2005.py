T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    
    tri_list = [1]
    for i in range(0,N):
        mid_list = tri_list[:]
        for j in range(1, i):
            tri_list[j] = mid_list[j]+mid_list[j-1]
        tri_list.append(1)
        
        for j in range(i+1):
            print(tri_list[j], end = ' ')
        print('')

        
                


    