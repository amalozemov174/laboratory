def Football(F, N):
    check = True
    variants = []
    for i in range(N - 1):
        if F[i] - F[i + 1] < 0:
            check = False
    if check:
        return check
    for i in range(N):
        for j in range(N):
            if i != j:
                tmp = F.copy() 
                tmp1 = F[i]
                tmp2 = F[j]
                tmp[i] = F[j]
                tmp[j] = F[i]
                variants.append(tmp)
    for i in range(len(variants)):
        check = True
        for j in range(len(variants[i]) - 1):
            tmp3 = variants[i][j + 1]
            tmp4 = variants[i][j]
            tmp34 = variants[i][j + 1] - variants[i][j]
            if variants[i][j + 1] - variants[i][j] < 0:
                 check = False
        if check:
            return check            
    return check
