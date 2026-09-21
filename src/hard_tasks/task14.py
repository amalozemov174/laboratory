def Unmanned(L: int, N: int, track: list):
    point_prev: int = 0
    result: int = 0
    time: int = 0
    length: int = L
    for i in range(N):
        tmp = track[i]
        point_svet = tmp[0]
        red = tmp[1]
        green = tmp[2]
        length = length - (point_svet - point_prev)
        time = time + (point_svet - point_prev)
        point_prev = point_svet
        delta_wait = time % (red + green)
        svet_wait = red - delta_wait
        if svet_wait > 0:
            time = time + svet_wait            
    time = time + length         
    return time
