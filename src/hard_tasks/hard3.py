def ConquestCampaign(N, M, L, battalion):
    day = 0
    map = []
    captured = []
    future_captured = []
    is_full = False
    for i in range(N):
        tmp = []
        for j in range(M):
           tmp.append(0) 
        map.append(tmp)
    while is_full != True:
        day += 1
        if day == 1:
            for b in range(0, L * 2, 2):
                is_used_first = True
                first_point_x = battalion[b] - 1
                first_point_y = battalion[b + 1] - 1
                map[first_point_x][first_point_y] = 1
                for fc in range(0, len(future_captured) - 1, 2):
                    if first_point_x == future_captured[fc] and first_point_y == future_captured[fc + 1]:
                         is_used_first = False
                if is_used_first:
                    future_captured.append(first_point_x)
                    future_captured.append(first_point_y)
        else:
            for index in range(0, len(captured), 2):
                index_x = captured[index]
                index_y = captured[index + 1]
                next_x = index_x + 1
                next_y = index_y + 1
                prev_x = index_x - 1
                prev_y = index_y - 1
                if next_x >= 0 and next_x <= N - 1 and map[next_x][index_y] != 1:
                    map[next_x][index_y] = 1
                    future_captured.append(next_x)
                    future_captured.append(index_y)
                if next_y >= 0 and next_y <= M - 1 and map[index_x][next_y] != 1:
                    map[index_x][next_y] = 1
                    future_captured.append(index_x)
                    future_captured.append(next_y)
                if prev_x >= 0 and prev_x <= N - 1 and map[prev_x][index_y] != 1:
                    map[prev_x][index_y] = 1
                    future_captured.append(prev_x)
                    future_captured.append(index_y)
                if prev_y >= 0 and prev_y <= M - 1 and map[index_x][prev_y] != 1:
                    map[index_x][prev_y] = 1
                    future_captured.append(index_x)
                    future_captured.append(prev_y)                                                 
        captured.clear()                                                                                 
        captured.extend(future_captured) 
        future_captured.clear()
        is_full = True
        for i1 in range(N):
            for j1 in range(M):
                if map[i1][j1] == 0:
                    is_full = False
                    break
    return day