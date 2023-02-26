# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this"

def who_likes_it(names):
    n = len(names)
    if len == 0:
        return "no one likes this"
    if len == 1:
        return f"{names[0]} likes this"
    if n == 2:
        return f"{names[0]} and {names[1]} likes this"
    if n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} likes this"
    if n >= 4:
        return f"{names[0]}, {names[1]} and 2 others likes this"
        
print(who_likes_it(["Alex", "Jacob", "Mark", "Max"]))
    