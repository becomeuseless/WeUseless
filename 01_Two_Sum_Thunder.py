"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


{7:0, 2: 1, -2: 3, -6: 4}

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        result = [None] * 2
        for i in range(len(nums)):
            if diff.get(nums[i]) is not None:
                result[0] = i
                result[1] = diff[nums[i]]
                break
            diff[target - nums[i]] = i
        return result