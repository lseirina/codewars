# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6

def digital_root(num):
    while num > 9:
        digit_sum = 0
        for digit in str(num):
            digits = int(digit)
            digit_sum += digits
        num = digit_sum
    return num

   
      
print(digital_root(942))