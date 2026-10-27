def TransformTransform(A, N):
    middle_res = SubTransform(A)
    final_res = SubTransform(middle_res)
    summ = 0
    for i in range(len(final_res)): 
        summ += final_res[i]
    if summ % 2 != 0:
        return False
    return True

def SubTransform(L):
    B = []
    k = -1
    for i in range(0, len(L)):
        for j in range(0, len(L) - i):
            k = i + j
            tmp_max = -1
            for m in range(j, k + 1):
                if L[m] > tmp_max:
                    tmp_max = L[m]
            B.append(tmp_max)
    return B   
