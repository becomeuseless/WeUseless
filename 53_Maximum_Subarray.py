
"""
init:
    global max = first element
    local max  = first element
    
for each element in list
    1. if current local < 0, all element before should be ignored.
    2. set current local to next since previous total is neg.
    3. global max = (previous max, current max)
    
    return global max
    
Space   O(1)
Time    O(n)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #edge case
        if not nums: 
            return None
        
        max_so_far = nums[0]
        max_ending_here = nums[0]
        
        for each in nums[1:]:
            if max_ending_here < 0:
                max_ending_here = each
            else:
                max_ending_here += each
            max_so_far = max(max_ending_here, max_so_far)
                
        return max_so_far
