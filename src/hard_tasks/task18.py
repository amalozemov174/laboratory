def MisterRobot(N, data):
    tmp_list = list(data)
    res = True
    minElement = min(tmp_list)
    index_min = tmp_list.index(minElement)
    for i in range(N - 2):
        min_val = tmp_list[i]
        for k in range(i, N):
            if tmp_list[k] < min_val:
                min_val = tmp_list[k]
        index_min = tmp_list.index(min_val)
        while index_min > i:  
            if index_min - i <= 1:
                tmp1 = tmp_list[i]
                tmp2 = tmp_list[i+1]
                tmp3 = tmp_list[i+2]             
                tmp_list[i] = tmp2
                tmp_list[i+1] = tmp3
                tmp_list[i+2] = tmp1
                index_min = i
            else:
                tmp1 = tmp_list[index_min]
                tmp2 = tmp_list[index_min - 1]
                tmp3 = tmp_list[index_min - 2]
                tmp_list[index_min - 2] = tmp1
                tmp_list[index_min - 1] = tmp3
                tmp_list[index_min] = tmp2
                index_min = index_min - 2
    if tmp_list != sorted(data):
        res = False
    return res
