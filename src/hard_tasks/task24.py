def MatrixTurn(Matrix, M, N, T):
    matrix_real = []
    layer = M
    if M > N:
        layer = N        
    for i in range(M):
        tmp = []
        for j in range(N):
            tmp.append(int(Matrix[i][j]))
        matrix_real.append(tmp)
    all_layer = []
    all_layer1 = []
    for l in range(layer):   
        tmp = []
        all_layers = {}
        for i in range(0, 1):
            for j in range(0, N - 1):
                tmp_i = i
                tmp_j = j
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(0, M - 1):
            for j in range(N - 1, N):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(M - 1, M):
            for j in range(N - 1, 0, -1):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(M - 1, 0, -1):
            for j in range(0, 1):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        all_layer.append(tmp)
        all_layer1.append(all_layers)
        tmp_mtrx = []
        for i in range(M):
            tmp = []
            for j in range(N):
                if matrix_real[i][j] != 0: 
                    tmp.append(int(matrix_real[i][j]))
            if len(tmp) != 0:
                tmp_mtrx.append(tmp)
        matrix_real = tmp_mtrx
        if len(matrix_real) == 0:
            break
        N = N - 2
        M = M - 2
    for i in range(len(all_layer)):
        for t1 in range(T):
            all_layer[i].insert(0, all_layer[i].pop())
    #for l in range(layer):
        
            
MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)            
