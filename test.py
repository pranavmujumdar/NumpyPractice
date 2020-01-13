def sum_of_Lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i ) for j in range(N)]
        total +=sum(L)
        del L
    return total
