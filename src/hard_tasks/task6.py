import math

def PatternUnlock(N, hits):
    lenght = 0
    used_ids = {}
    used_ids[1] = [0,1]
    used_ids[2] = [1,1]
    used_ids[3] = [2,1]
    used_ids[4] = [2,0]
    used_ids[5] = [1,0]
    used_ids[6] = [0,0]
    used_ids[7] = [2,2]
    used_ids[8] = [1,2]
    used_ids[9] = [0,2]
    for i in range(N - 1):
        curr = used_ids.get(hits[i])
        next = used_ids.get(hits[i + 1])
        tmp1 = curr[0]
        tmp2 = curr[1]
        next1 = next[0]        
        next2 = next[1]
        if curr[0] == next[0] or curr[1] == next[1]:
            lenght += 1
        else:
            lenght += math.sqrt(2)       
    lenght = round(lenght, 5)
    len_final = ''
    for j in str(lenght):
        if j == '.':
            continue 
        if int(j) != 0:
            len_final += j            
    return len_final    