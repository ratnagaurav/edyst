def get_unset_bits(num):
    unset_bits = []
    for i in range(0, 31):
        if ((1 << i) & num ) == 0:
            unset_bits.append(i)
    
    return unset_bits



T = int(input())

for case in range(T):
    N, Q = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    assert len(arr)  == N
    
    #optimal approach
    zeros = [[0 for _ in range(31)] for _ in range(N)]  # creating the prefix sum array


    # record v's contribution to each range by increasing/descreasing in a range

    for query in range(Q):
        l, r, v = list(map(int, input().split()))
        unset_bits = get_unset_bits(v) 
        for i in unset_bits:
            zeros[l-1][i]+= 1
            if r < N:
                zeros[r][i]-= 1
            
    for i in range(1,len(zeros)):
        for j in range(len(zeros[i])):
            zeros[i][j] = zeros[i][j]+zeros[i-1][j] # calculate prefix sum

    for i in range(len(arr)):
        bitmask = 0
        for j in range(len(zeros[i])):
            if zeros[i][j]<=0:
                bitmask = bitmask + 2**j
        arr[i] = arr[i] & bitmask
        print(arr[i], end = ' ')
    print()