def SherlockValidString(s):
    res = False
    dict_vars = []
    if len(s) == 0:
        return True
    dict_vars.append(s)
    for i in range(len(s)):
        temp = ''
        for j in range(len(s)):
            if i != j:
                temp += s[j]
        dict_vars.append(temp)
    dict_words = {}    
    for w in dict_vars:
        for c in w:
            if dict_words.get(c, 0) == 0:
                dict_words[c] = 1
            else:
                dict_words[c] = dict_words.get(c, 0) + 1                
        min_var = min(dict_words.values())        
        for k,v in dict_words.items():
            if v != min_var:
                res = False
                dict_words = {}
                break
            else:
               res = True
        if res:
            return True
    return res 
