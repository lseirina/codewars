# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

def get_outlier(nums):
    even_nums = []
    odd_nums = []
    for i in nums:
        if i % 2 == 0:
            even_nums.append(i)
            
        else:
            odd_nums.append(i)
    if len(even_nums) == 1:
        return even_nums[0]
    else:
        return odd_nums[0]     
    

print(get_outlier([160, 3, 1719, 19, 11, 13, -21]))


           
        
        
        