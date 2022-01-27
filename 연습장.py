# a = 'asdfasdf'
# for st in a:
#     print(st, end = ' ')     #a s d f a s d f 



# a = 'asdfasdfasdf'
# b = a[0:4]
# print(a[0:4])              # asdf
# c = a[4:8]
# print(a[4:8])

# print(bool(b == c))         #True



# a = 'asdfasdfasdf'
# i = 2
# b = a[0:4]
# print(a[0:4])              # asdf
# c = a[2*i:4*i]
# print(a[4:8])

# print(bool(b == c))    #True



# N = 5
# tri_list = [i for i in range(N)]
# for i in range(N):
#     tri_list[i] = [1]

# print(tri_list)                # [[1], [1], [1], [1], [1],]



# N = 5
# tri_list = [[i] for i in range(N)]


# print(tri_list)       # [[0], [1], [2], [3], [4]]





# M, N = map(int, input().split())                                    # M = 3
# sq_list = []

# for i in range(M):
#     a = list(map(int, input().split()))                           # 1 2 3  \n  4 5 6  \n 7 8 9
#     sq_list.append(a)                             

# print(sq_list)                                                    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]       







# a = list(map(int, input().split()))             # input = 1 2 3 4 5 6
# print(a)                                        #[1,2,3,4,5,6]


# a = list(map(int, input().split()))           # 99 5 4
# a.remove(max(a))
# print(a)                                      #  5  4




# for i in range(5):
#     print('hi'* i)                # hi    hihi     hihihihi       hihihihihi

# a = [2, 4, 99, 1]
# a.sort()
# print(a)                          # [1, 2, 4, 99]





# a = [1,1,1,1,0]
# for i in range(len(a)-2):

#     print(a[i:i+3])                     #[1, 1, 1]
#                                         #[1, 1, 1]
#                                         #[1, 1, 0]


puzzl_list = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
K= 3
for i in range(5):
    for j in range(2):
        print(puzzl_list[j:j+K][i])