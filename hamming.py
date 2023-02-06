# hamming_distance('100101', '101001') == 2
# hamming_distance('1010', '0101') == 4
# hamming("I like turtles","I like turkeys")  //returns 3
# hamming("Hello World","Hello World")  //returns 0
def hamming(a, b):
    diff = []
    i = 0
    
    while i < len(a):
        if a[i] != b[i]:
            diff.append(a[i])
        i += 1
                    
    return len(diff)

print(hamming("Hello World","Hello World"))