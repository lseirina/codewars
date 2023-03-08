# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

def count_duplicates(string):
    counts = []
    repeating_char = set()
    
    for i in string.lower():
        if i in counts:
           repeating_char.add(i)
        counts.append(i)
        
    return len(repeating_char)

print(count_duplicates("ABBA"))
        
        
        