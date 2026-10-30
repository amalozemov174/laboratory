def white_walkers(village):
    substr_id = []
    chains = []
    counts = 0
    res = False
    staright_count = 0
    start_number = -1
    end_number = -1
    is_start_num = False
    substr = ''
    if len(village) < 5:
        return False
    for i in range(len(village)):
        if village[i].isnumeric():
            if is_start_num != True:
                is_start_num = True
                start_number = int(village[i])
                substr += village[i]
            else:
                substr += village[i]
                end_number = int(village[i])
                if start_number + end_number == 10:
                    chains.append(substr)
                substr = ''
                substr = village[i]
                start_number = int(village[i])
        else:
            if is_start_num:
                substr += village[i]
    for ch in chains:
        for rg in range(1, len(ch)):
            tmp = ch[rg]
            if ch[rg] == '=':
                counts += 1
        if counts != 3:
            return False
        else:
            res = True
            counts = 0
    return res
