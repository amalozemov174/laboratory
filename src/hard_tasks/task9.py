import math

def TheRabbitsFoot(s: str, encode: bool) -> str:
    if encode:
        s_res: str = s.replace(' ', '')
        res_sqrt: float = math.sqrt(len(s_res))
        column: int = math.ceil(res_sqrt) 
        strs: int = math.floor(res_sqrt)
        if len(s_res) > column * strs:
            strs += 1
        tmp_res: list = []
        str_el: int = 0
        for i in range(strs):
            line = []
            tmp_res.append(line)
            for j in range(column):
                if str_el >= len(s_res):
                    line.append(None)
                else:    
                    line.append(s_res[str_el])
                str_el += 1
        str_final: str = ''        
        for m in range(column):
            for k in range(strs):
                if tmp_res[k][m] is not None: 
                    str_final += tmp_res[k][m]
            str_final += ' '    
        return str_final             
    else:
        s_res: list = s.replace(' ', '')
        res_sqrt: float = math.sqrt(len(s_res))
        column: int = math.ceil(res_sqrt) 
        strs: int = math.floor(res_sqrt)
        if len(s_res) > column * strs:
            strs += 1
        tmp_res: str = ''
        str_el: int = 0
        matrix: list = []
        for i in range(strs):
            row: list = []
            for j in range(column):
                row.append(None)
            matrix.append(row)   
        for j in range(column):
            for i in range(strs):
                if i * column + j < len(s_res):
                    matrix[i][j] = s_res[str_el]
                    str_el += 1
        tmp_res: str = ''
        for i in range(strs):
            for j in range(column):
                if matrix[i][j] is not None:
                    tmp_res += matrix[i][j]           
        return tmp_res 