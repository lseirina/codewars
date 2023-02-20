# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
def get_middle(word):
    length = len(word)
    if length % 2 != 0:
        middle_index = int(length / 2)
        return word[middle_index]
    else:
        middle_index = int(length / 2) - 1
        return word[middle_index:middle_index+2]   
print(get_middle("test"))