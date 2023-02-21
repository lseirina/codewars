# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

def square(num):
    if num < 0:
        return False
    i = 0
    while i < num:
        if i * i == num:
            return True
        i += 1
    return False

print(square(4))