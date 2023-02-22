# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
"""
def get_multiple(num):
    if num < 0:
        return 0
    my_list = []
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            my_list.append(i)
                
    return sum(my_list)

print(get_multiple(15))  

    """
def sum_multiple(num):
    if num < 0:
        return 0
    sum = 0
    
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_multiple(15))

