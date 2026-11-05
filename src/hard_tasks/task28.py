def Keymaker(k):
    keys = []
    res = ''
    for i in range(k):
        keys.append(0)
    for i in range(k):
        for j in range(k):
            if (j + 1) % (i + 1) == 0:
                if keys[j] == 0:
                    keys[j] = 1
                else:
                    keys[j] = 0
    for i in range(k):
        res += str(keys[i])
    return res 
