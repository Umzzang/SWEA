T = int(input())
for i in range(1, T+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        for j in str(i):
            if j == '3' or j == '6' or j == '9':
                print('-', end ='')
        print('', end = ' ')
    else:
        print(i, end = ' ')
        