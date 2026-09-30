def LineAnalysis(line: str) -> bool:
    line_split: list = line.split('*')
    res: bool = True    
    tmp = line_split[1]
    for i in range(2, len(line_split) - 1):
        if tmp != line_split[i]:
            return False
    return res
