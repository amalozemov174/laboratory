def BigMinus(s1, s2):
    bigger = ''
    less = ''
    isEqual = False
    if len(s1) > len(s2):
        bigger = s1
        less = s2
    elif len(s2) > len(s1):
        bigger = s2
        less = s1
    elif len(s2) == len(s1):
        for i in range(len(s2)):
            isEqual = True
            if int(s2[i]) > int(s1[i]):
                bigger = s2
                less = s1
                isEqual = False
                break
            elif int(s2[i]) < int(s1[i]):
                bigger = s1
                less = s2
                isEqual = False
                break
    if isEqual:
        return '0'
    for i in range(len(bigger) - len(less)):
        less = '0' + less
    isless = False
    vychitaemome = 0
    tmp_res = ''
    for i in range(len(bigger) - 1, -1, -1):
        if isless:
            vychitaemome = int(bigger[i]) - 1
        else:
            vychitaemome = int(bigger[i])
        if vychitaemome < int(less[i]):
            tmp_res = str(vychitaemome - int(less[i]) + 10) + tmp_res
            isless = True
        else:
            tmp_res = str(vychitaemome - int(less[i])) + tmp_res
    if tmp_res[0] == '0' and len(tmp_res) == 1:
        return tmp_res
    while tmp_res[0] == '0':
        tmp_res = tmp_res[1:]
    return tmp_res
