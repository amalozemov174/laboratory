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
    start_i = 0 
    start_j = 0
    end_i = M
    end_j = N
    for l in range(layer // 2):   
        tmp = []
        all_layers = {}
        for i in range(start_i, start_i + 1):
            for j in range(start_j, end_j - 1):
                tmp_i = i
                tmp_j = j
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(start_i, end_i - 1):
            for j in range(end_j - 1, end_j):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(end_i - 1, end_i):
            for j in range(end_j - 1, start_j, -1):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        for i in range(end_i - 1, start_i, -1):
            for j in range(start_j, start_j + 1):
                tmp_i = i
                tmp_j = j                
                tmp.append(matrix_real[i][j])
                all_layers[(i,j)] = matrix_real[i][j]
                matrix_real[i][j] = 0
        all_layer.append(tmp)
        all_layer1.append(all_layers)
        tmp_mtrx = []
        if len(matrix_real) == 0:
            break
        start_i += 1 
        start_j += 1
        end_i -= 1
        end_j -= 1
                        
    for i in range(len(all_layer)):
        for t1 in range(T):
            all_layer[i].insert(0, all_layer[i].pop())
    res_matrix = []
    for i in range(M):
        tmp = []
        for j in range(N):
            tmp.append(0)
        res_matrix.append(tmp)    
    for i in range(len(all_layer)):
        layer_elements = all_layer[i]
        layer_coords = list(all_layer1[i].keys())        
        for idx in range(len(layer_elements)):
            coord = layer_coords[idx]
            res_matrix[coord[0]][coord[1]] = layer_elements[idx]
    final_result = []
    for row in res_matrix:
        string_row = ""
        for number in row:
            string_row += str(number)
        final_result.append(string_row)
        
    return final_result
