T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    grade_list = []
    for i in range(N):
        middle, final, homework = map(int, input().split())
        grade = middle * 0.35 + final * 0.45 + homework * 0.2
        grade_list.append(grade)
    
    want_grade = grade_list[K-1]

    grade_list.sort()
    grade_list.reverse()
    for i in range(len(grade_list)):
        if grade_list[i] == want_grade:
            gra = i+1
            break
    if gra/N <= 0.1 :
        want_gra = 'A+'
    elif gra/N <= 0.2 :
        want_gra = 'A0'
    elif gra/N <= 0.3 :
        want_gra = 'A-'
    elif gra/N <= 0.4 :
        want_gra = 'B+'
    elif gra/N <= 0.5 :
        want_gra = 'B0'
    elif gra/N <= 0.6 :
        want_gra = 'B-'
    elif gra/N <= 0.7 :
        want_gra = 'C+'
    elif gra/N <= 0.8 :
        want_gra = 'C0'
    elif gra/N <= 0.9 :
        want_gra = 'C-'
    else:
        want_gra = 'D0'
    print(f'#{test_case} {want_gra}')