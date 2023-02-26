# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
#[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""
def find_odd_int(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count % 2 != 0:
            return num
"""

def find_odd_int(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    for num, count in counts.items():
        if count % 2 != 0:
            return num

print(find_odd_int([1,2,2,3,3,3,4,3,3,3,2,2,1]))    

