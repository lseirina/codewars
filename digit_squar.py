#765 = 493625

def square_digit(num):
    result = ""
    for i in str(num):
        square = int(i)**2
        result += str(square)
        
    return int(result)
        
    

print(square_digit(765))