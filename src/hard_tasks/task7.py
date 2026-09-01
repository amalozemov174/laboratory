def WordSearch(lens, s, subs):
    res = []
    space_index = -1
    res_str = ''
    strs = []
    start_substr = 0
    end_substr = 11
    move_index = 0
    count_space = 0
    len_substr = lens + move_index
    end = True
    while end:
        len_substr = lens + move_index
        if len_substr > len(s):
            len_substr = len(s)
        for i in range(move_index, len_substr):
            if s[i] == ' ':
                space_index = i
                res_str += s[i]
                count_space += 1
            else:
                res_str += s[i]
        if len_substr == len(s):
            strs.append(res_str)
            end = False
            continue
        tmp2 = s[len_substr]         
        if s[len_substr] == ' ':
            strs.append(res_str)
            move_index = len_substr
            res_str = ''
        elif space_index == -1:    
            strs.append(res_str)
            move_index = len_substr
            res_str = ''
        else:
            final_str = ''
            for s1 in res_str:
                if s1 != ' ' and count_space >= 1:
                    final_str += s1
                elif s1 == ' ' and count_space >= 1:
                    final_str += s1
                    count_space -= 1
                else:
                    res_str = final_str
                    break    
            if final_str != ' ':
                strs.append(final_str.strip())
            if space_index == -1:
                move_index = move_index + 1
            else:    
                move_index = space_index + 1
                space_index = -1
            res_str = ''            
    for name in strs:
        find = 0
        words = name.split()
        for w in words:
            if find == 1:
                break
            if len(subs) == len(w):
                for m in range(len(subs)):
                    find = 1
                    if subs[m] != w[m]:
                        find = 0
                        break
            else:
                find = 0
        res.append(find)
    return res
