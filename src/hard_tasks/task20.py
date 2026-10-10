current_str = ''
command_list = []

def BastShoe(command):
    global current_str
    global command_list
    if len(command) <= 0:
        return current_str
    task = int(command.split()[0])
    if task == 1:
        if len(command_list) > 0:
            tmp1 = command_list[len(command_list) - 1]
            tmp2 = tmp1.split()
            delete_i = []
            if int(command_list[len(command_list) - 1].split()[0]) == 4:
                for i in range(len(command_list)):
                    prevs_task = int(command_list[i].split()[0])
                    if prevs_task != 1 and prevs_task != 2:
                        delete_i.append(command_list[i])
                #command_list = delete_i
                command_list = []
        text = command.split(maxsplit=1)[1]
        command_list.append(command + ' ' + '#' + current_str)
        current_str += text         
    elif task == 2:
        if len(command_list) > 0:
            if int(command_list[len(command_list) - 1].split()[0]) == 4:
                command_list = []
        del_elem = int(command.split()[1])
        command_list.append(command + ' ' + '#' +  current_str)
        if del_elem > len(current_str):
            current_str = ''
        else:    
            current_str = current_str[:-del_elem]
    elif task == 3:     
        get_elem = int(command.split()[1])
        command_list.append(command)
        return current_str[get_elem]
    elif task == 4:
        temp_i = -1
        if len(command_list) == 1:
            prev_task = int(command_list[0].split()[0])
            if prev_task == 1 or prev_task == 2:
                temp_i = 0
                command_list.append(command + ' ' + current_str)
                #tmp4 = command_list[i].split(maxsplit=2)
                tmp4 = command_list[0].split('#')
                #current_str = command_list[i].split(maxsplit=2)[2]
                current_str = command_list[0].split('#')[1]
            elif prev_task == 5:
                temp_i = 0
                command_list.append(command + ' ' + current_str)
                tmp4 = command_list[0].split(maxsplit=1)
                current_str = command_list[0].split(maxsplit=1)[1]     
        for i in range(len(command_list) - 1, 0, -1):
            prev_task = int(command_list[i].split()[0])
            if prev_task == 1 or prev_task == 2:
                temp_i = i
                command_list.append(command + ' ' + current_str)
                #tmp4 = command_list[i].split(maxsplit=2)
                tmp4 = command_list[i].split('#')
                #current_str = command_list[i].split(maxsplit=2)[2]
                current_str = command_list[i].split('#')[1]
                break
            elif prev_task == 5:
                temp_i = i
                command_list.append(command + ' ' + current_str)
                tmp4 = command_list[i].split(maxsplit=1)
                current_str = command_list[i].split(maxsplit=1)[1]     
                break
        if temp_i > 0:    
            command_list.pop(temp_i)
    elif task == 5:
        temp_i = -1     
        for i in range(len(command_list) - 1, 0, -1):
            prev_task = int(command_list[i].split()[0])
            if prev_task == 4:
                temp_i = i
                command_list.append(command + ' ' + current_str)
                #tmp4 = command_list[i].split(maxsplit=2)
                tmp5 = command_list[i].split(maxsplit=1)
                #current_str = command_list[i].split(maxsplit=2)[2]
                current_str = command_list[i].split(maxsplit=1)[1]
                break
        if temp_i > 0:     
            command_list.pop(temp_i)    
    else:
        return current_str
    return current_str
