text = "hello, my name is Ira"
my_list = []

for i in text.lower():
    if i in ("a", "e", "u", "o", "i"):
        my_list.append(i)
        
print(len(my_list))
    