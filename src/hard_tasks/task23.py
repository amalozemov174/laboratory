def TreeOfLife(H, W, N, tree):
    arr = []
    for i in range(H):
        row = []
        for j in range(W):
            row.append(0)
        arr.append(row)
    for m in range(len(tree)):
        for n in range(len(tree[m])):
            if tree[m][n] == '.':
                arr[m][n] = 0
            else:
                arr[m][n] = 1            
    for l in range(1, N + 1):
        for m in range(len(tree)):
            for n in range(len(tree[m])):
                arr[m][n] = arr[m][n] + 1
        if l%2 == 0:
            for m in range(len(tree)):
                for n in range(len(tree[m])):
                    if arr[m][n] >= 3:
                        index_x = m
                        index_y = n
                        next_x = index_x + 1
                        next_y = index_y + 1
                        prev_x = index_x - 1
                        prev_y = index_y - 1
                        if next_x >= 0 and next_x <= H - 1 and arr[next_x][index_y] <= 3:
                            arr[next_x][index_y] = 0
                        if next_y >= 0 and next_y <= W - 1 and arr[index_x][next_y] <= 3:
                            arr[index_x][next_y] = 0
                        if prev_x >= 0 and prev_x <= H - 1 and arr[prev_x][index_y] <= 3:
                            arr[prev_x][index_y] = 0
                        if prev_y >= 0 and prev_y <= W - 1 and arr[index_x][prev_y] <= 3:
                            arr[index_x][prev_y] = 0
                        arr[index_x][index_y] = 0
    for m in range(len(tree)):
        for n in range(len(tree[m])):
            if arr[m][n] == 0:
                arr[m][n] = '.'
            else:
                arr[m][n] = '+'
    return arr 
