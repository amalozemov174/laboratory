def ShopOLAP(N, items):
    res = {}
    for i in range(N):
        tmp = items[i].split(' ')
        key_tmp = tmp[0]
        key_value = int(tmp[1])
        if res.get(key_tmp) is not None:
            res[key_tmp] = res.get(key_tmp) + key_value
        else:
            res[key_tmp] = key_value
    sorted_data = dict(sorted(res.items()))
    sorted_data1 = dict(sorted(sorted_data.items(), key=lambda item: item[1], reverse=True))
    return sorted_data1
