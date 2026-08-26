def odometer(oksana):
    length = 0
    prev_time = 0
    for i in range(0, len(oksana) - 1, 2):
        length += oksana[i] * ( oksana[i + 1] - prev_time)
        prev_time = oksana[i + 1]
    return length 


print(odometer([10,1,20,2]))