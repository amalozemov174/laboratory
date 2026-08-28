def SynchronizingTables(N, ids, salary):
    salary_sorted = sorted(salary)
    salary_undo = []
    ind = 0
    for make_idx in range(N):
        salary_undo.append(ind)
    used_ids = {}
    next_salary = N - 1
    for i in ids:
        used_ids[i] = 0
    continue_search = True
    while continue_search:
        for key_f in used_ids.keys():
            if used_ids.get(key_f) == 0:
                continue_search = True    
            else:
                continue_search = False
            for j in range(N):
                if used_ids.get(ids[j]) == 0:
                    next = ids[j]
                    index_next_max = j
                    for j1 in range(N):
                        if used_ids.get(ids[j1]) == 0:
                            a = ids[j1]
                            if a > next:
                                next = ids[j1]
                                index_next_max = j1
                    if used_ids.get(ids[index_next_max]) == 0:
                        used_ids[ids[index_next_max]] = 1
                        t = ids.index(next)
                        salary_undo[t] = salary_sorted[next_salary]
                        next_salary -= 1     
    return salary_undo