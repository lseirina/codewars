txt =  "This website is for losers LOL!"
def remove_vowels(a):
   
    for i in a.lower():
        if i in ("e","u", "i", "o", "a", "E", "U", "O"): 
            a = a.replace(i, "")
    return a


print(remove_vowels(txt))
            