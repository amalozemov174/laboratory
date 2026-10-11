current_str = ''
undo_list = []
redo_list = []
is_undo = False

def BastShoe(command):
    global current_str
    global redo_list
    global undo_list
    global is_undo
    if len(command) <= 0:
        return current_str
    task = int(command.split()[0])
    if task == 1:
        if is_undo:
            undo_list = []
            redo_list = []
            is_undo = False             
        text = command.split(maxsplit=1)[1]
        undo_list.append(current_str)
        current_str += text         
    elif task == 2:
        if is_undo:
            undo_list = []
            redo_list = []
            is_undo = False
        del_elem = int(command.split()[1])
        undo_list.append(current_str)
        if del_elem > len(current_str):
            current_str = ''
        else:    
            current_str = current_str[:-del_elem]
    elif task == 3:     
        get_elem = int(command.split()[1])
        if get_elem >= len(current_str) or get_elem < 0:
            return ''    
        return current_str[get_elem]
    elif task == 4:
        is_undo = True
        if len(undo_list) > 0:
            redo_list.append(current_str)
            current_str = undo_list.pop()                            
    elif task == 5:
        if len(redo_list) > 0:
            undo_list.append(current_str)
            current_str = redo_list.pop()            
    else:
        return current_str
    return current_str
