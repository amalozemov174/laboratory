def BiggerGreater(input):
    res = ''
    make_str = ''
    mass = []
    russian_words = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ё':6, 'ж':7, 'з':8, 'и':9, 'й':10, 'к':11, 'л':12, 'м':13, 'н':14, 'о':15, 'п':16, 'р':17, 'с':18, 'т':19, 'у':20, 'ф':21, 'х':22, 'ц':23, 'ч':24, 'ш':25, 'щ':26, 'ъ':27, 'ы':28, 'ь':29, 'э':30, 'ю':31, 'я':32}
    russian_words_rev = {0:'а', 1:'б', 2:'в', 3:'г', 4:'д', 5:'е', 6:'ё', 7:'ж', 8:'з', 9:'и', 10:'й', 11:'к', 12:'л', 13:'м', 14:'н', 15:'о', 16:'п', 17:'р', 18:'с', 19:'т', 20:'у', 21:'ф', 22:'х', 23:'ц', 24:'ч', 25:'ш', 26:'щ', 27:'ъ', 28:'ы', 29:'ь', 30:'э', 31:'ю', 32:'я'}
    english_words = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    english_words_rev = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
    current_words = russian_words
    current_words_rev = russian_words_rev
    if russian_words.get(input[0], -1) < 0:
        current_words = english_words
        current_words_rev = english_words_rev
    for k in range(len(input)):
        mass.append(current_words.get(input[k]))
    dict_all_range = []
    for i in range(len(mass)):
        for j in range(len(mass)):
            if i == j:
                continue
            tmp = mass.copy()
            tmp1 = tmp[i]
            tmp2 = tmp[j]
            tmp[i] = tmp2
            tmp[j] = tmp1
            if tmp[i] > mass[i] and i < j:
                tail = sorted(tmp[i+1:])    
                tmp = tmp[:i+1] + tail
            dict_all_range.append(tmp)          
    #print(dict_all_range)            
    sort_vals = sorted(dict_all_range)    
    #print(sort_vals)
    for m in range(len(sort_vals)):
        tmp4 = sort_vals[m]
        #print(tmp4)            
        for l in range(len(sort_vals[m])):
            tmp3 = sort_vals[m][l]
            #print(tmp3)            
            make_str += current_words_rev.get(sort_vals[m][l])
        #print(make_str)    
        if make_str > input:
            return make_str
        else:
            make_str = ''
    return res
