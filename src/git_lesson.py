def count_words(s: str) -> int:
    sl: List[str] = list(s)
    count: int = 0
    is_word: bool = False
    for i in range(len(sl)):
        if sl[i] != ' ':
            if is_word != True:
                count += 1
                is_word = True
        else:
            is_word = False
    return count
def min_number(n1: int, n2: int, n3: int) -> int:
    min: int = n1
    if n2 <= min:
        min = n2
    if n3 <= min:
        min = n3        
    return min
def min_string(s1: str, s2: str, s3: str):
    return min_number(count_words(s1), count_words(s2), count_words(s3))
print(min_string('   5678 91011 4444  ', '     12345 5678 91011 4444  5555', ' 555 12345 5678 91011 4444 666'))
