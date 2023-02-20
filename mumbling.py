# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def mumble(word):
    my_list = []
    
    for i in range(len(word)):
        my_list.append(word[i]*(i+1))
    
    mumble_word = "-".join(my_list)
    return mumble_word.title() 
    

print(mumble("RqaEzty"))
