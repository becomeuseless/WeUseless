"""
198. House Robber
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

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
	"""
	Time: O(N)
	Space: O(1)
	Thanks for Shisui.
	"""
        # two variables, prev and curr
        pMax,cMax = 0,0
        for each in nums:
            holder = cMax #max not including current element
            cMax = max(cMax, pMax + each)
            pMax = holder #pMax

    """Iterative from back to front find a maximum value"""
    def rob2(self, nums: List[int]) -> int:
        memo = {}
        #print(id(memo))
        if not nums:
            return 0
        return self.robHelper(nums, len(nums)-1, memo)
        
        
    def robHelper(self, nums: List[int], i: int, memo: dict()):
        """
        :type nums: List[int]
        :i: current position
        :memo: memoization to optimize same call
        
        time: O(N)
        space: O(N)
        """
        #print(id(memo))
        if i in memo:           #if helper(list, i, memo) already been called
            return memo[i]
        elif i < 0:             #base cases
            return 0
        elif i == 0:
            return nums[0]
        elif i == 1:
            return max(nums[0], nums[1])
        else:
            res = max(self.robHelper(nums, i-2, memo) + nums[i], self.robHelper(nums, i-1, memo))
            memo[i] = res
            return res