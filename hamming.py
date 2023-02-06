# hamming_distance('100101', '101001') == 2
# hamming_distance('1010', '0101') == 4

def hamming(a, b):
    diff = []
    i = 0
    
    while i < len(a):
        if a[i] != b[i]:
            diff.append(a[i])
        i += 1
                    
    return len(diff)

print(hamming("1010","0101"))