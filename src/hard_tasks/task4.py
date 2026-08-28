def MadMax(N, Tele):
    if N == 1:
        return Tele
    sort = sorted(Tele)
    middle_index = (N - 1) // 2
    max_index = N - 1
    max_val = sort[max_index]
    middle = sort[middle_index]
    sort[max_index] = middle
    sort[middle_index] = max_val
    for j in range(max_index, middle_index, -1):
        curr = sort[j]
        for i in range(max_index, middle_index, -1):
            compare = sort[i]
            if curr < compare:
                sort[j] = compare
                sort[i] = curr
                curr = sort[j]
                continue
    return sort