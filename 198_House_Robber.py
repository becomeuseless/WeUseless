'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

class Solution(object):
    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #Option 1: recursive 
        #Time Complextiy: O(2**n)
        #Space Complexity: O(n)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        return max(self.rob(nums[2:]) + nums[0], self.rob(nums[1:]))
        '''

        #Option 1 improved: recursive and memoization
        #Time Complextiy: O(n)
        #Space Complexity: O(n)
        return self.helper(nums, len(nums)-1)

    def __init__(self):
        self.memo = {}

    def helper(self, nums, i):
        if i in self.memo :
            return self.memo[i]
        elif i < 0 :
            return 0
        elif i == 0 :
            return nums[0]
        elif i == 1 :
            return max(nums[0],nums[1])
        else :
            res = max(self.helper(nums, i-2) + nums[i], self.helper(nums, i-1))
            self.memo[i] = res
            return res

        '''
        #Option 2: iterative. Use 2 variables, one keep the max amount by current house and one keep the max amount by the
        #previous house. Then iterative.
        #Time Complexity : O(n)
        #Space Complecity : O(1)

        cmax = 0
        pmax = 0

        for i in range(len(nums)):
            holder = cmax
            cmax = max(cmax, pmax + nums[i])
            pmax = holder

        return cmax
        '''
