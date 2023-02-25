#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 


def spin_words(words):
    split_words = words.split(" ")
    result = []
    for word in split_words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
            
    return " ".join(result)

print(spin_words("this is another test"))  



