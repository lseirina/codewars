#createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

def creat_phone_number(nums):
    
    for i in str(nums):
       result = "({0}) {1}-{2}".format(i[0],i[1],i[2], i[3],i[4],i[5], i[6],i[7],i[8],i[9])
       
    return result

print(creat_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


