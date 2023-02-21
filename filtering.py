# ilter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter(my_list):
    list_filter = []
    for i in my_list:
        try:
            if i == int(i):
                list_filter.append(i)
        except ValueError:
            pass
            
    return list_filter

print(filter([1,2,'aasf','1','123',123]))