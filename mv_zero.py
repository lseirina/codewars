#moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]


            
def move_zeros(arr):
    # non_zeros = [x for x in arr if x != 0 or isinstance(x, bool)]
    # num_zeros = len(arr) - len(non_zeros)
    # return non_zeros + [0] * num_zeros

    non_zeros = []
    for x in arr:
        if x != 0 or isinstance(x, bool) == True:
            non_zeros.append(x)
    num_zeros = len(arr) - len(non_zeros)
    return non_zeros + [0] * num_zeros
            
print(move_zeros([False,1,0,1,2,0,1,3,"a"]))