#arrayDiff([1,2,2,2,3],[2]) == [1,3]
"""
def arrayDiff(a, b):
    return [x for x in a if x not in b]
"""
def remove_common_elements(list1, list2):
    my_list = []
    for i in list1:
        if i not in list2:
            my_list.append(i)
            
    return my_list

print(remove_common_elements([1,2,2,2,3],[2]))
            
            
            
    


