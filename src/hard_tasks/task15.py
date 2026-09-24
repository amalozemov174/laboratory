def TankRush(H1, W1, S1, H2, W2, S2):
    res = False
    field1 = []
    field2 = []
    S1_split = S1.split()
    S2_split = S2.split()
    for i in range(H1):
        tmp = []
        for j in range(W1):
            tmp.append(int(S1_split[i][j]))
        field1.append(tmp)
    for k in range(H2):        
        tmp = []
        for m in range(W2):
            tmp.append(int(S2_split[k][m]))
        field2.append(tmp)    
    for x in range(H1 - H2 + 1):
        for y in range(W1 - W2 + 1):
            res = False
            for x1 in range(H2):
                for y1 in range(W2):
                    tmp_x = x
                    tmp_y = y
                    tmp_x1 = x1
                    tmp_y1 = y1
                    f1 = field1[x + x1][y + y1]
                    f2 = field2[x1][y1]
                    if f1 != f2:
                        res = False
                        break 
                    else:
                        res = True
            if res:
                break
    return res
