def UFO(N, data, octal):
    digits = '0123456789abcdef'
    result = []   
    if octal:
        base = 8
    else:
        base = 16
    if N == 0:
        result = []        
    for i in range(N):
        tmp_str = str(data[i])
        value = 0
        power = 0
        for char in reversed(tmp_str):
            digit_value = digits.index(char)            
            value += digit_value * (base ** power)
            power += 1            
        result.append(value)            
    return result
