def sortArray(input_array) :
    for i in range(len(input_array)):
        for j in range(len(input_array)):
            if i == j:
                continue;
            if input_array[j] > input_array[i]:
                tmp = input_array[i]
                input_array[i] = input_array[j]
                input_array[j] = tmp
    return input_array             