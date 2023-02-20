#Input: 42145 Output: 54421

def descending(numbers):
    num_list = []
    for num in str(numbers):
        num_list.append(num)
    num_list.sort(reverse=True)
    return int("".join(num_list))


print(descending(42145))