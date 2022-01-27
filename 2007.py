T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    long_str = input()
    def short_str(st):
        new_str = ''
        i = 0
        for j in range(i+1,len(long_str)):
            if st[i] == st[j] and st[0:j] == st[j:2*j]:
                

                return j

print(f'#{test_case} {short_str(long_str)}')

    
                



