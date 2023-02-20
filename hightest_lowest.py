# Kata.HighAndLow("1 2 3 4 5");  // return "5 1"
# Kata.HighAndLow("1 2 -3 4 5"); // return "5 -3"
# Kata.HighAndLow("1 9 3 4 -5"); // return "9 -5"


def highest_lowest(numbers):
    num_list = []
    for num in numbers.split( ):
        num_list.append(int(num))
        
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"

print(highest_lowest("1 2 3 4 5"))
    