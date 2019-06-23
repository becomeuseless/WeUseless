'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Option 1 : use dictionary
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        #Option 2 : math (rabbit and duck in the same cage). One single line code
        #Time Complexity : O(n)
        #Space Complexity : O(n)
        #return 2*sum(set(nums)) - sum(nums)

        #Option 3 : Bit manipulation
        #Time Complexity : O(n)
        #Space Comlexity : O(1)
        a = 0
        for n in nums :
            a ^= n
        return a
            
