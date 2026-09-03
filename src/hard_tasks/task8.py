def SumOfThe(N, data):
    sum_res = 0
    for i in range(N):
        for j in range(N):
            tmp1 = data[i]
            tmp2 = data[j]
            if i != j:
                sum_res += data[j]
        if sum_res == data[i]:
            return sum_res
        sum_res = 0
    return sum_res
