'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #Time Complexity : O(logn)
        #Space Complexity : O(1)

        '''
        test case:
        [1,3,5,6] 5 => 2
        [1,3,5,6] 7 => 4
        [1,3,5,6] 0 => 0
        '''

        lo = 0
        hi = len(nums)
        while (lo < hi) :
            mi = (lo + hi) >> 1
            if target <= nums[mi] : hi = mi
            else : lo = mi + 1
        return lo
            
    def searchInsert2(self, nums: List[int], target: int) -> int:
        """Binary Search to locate the value"""
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[(l+r)//2] == target:
                return (l+r)//2
            elif nums[(l+r)//2] > target:
                r = (l + r) //2 -1
            elif nums[(l+r)//2] < target:
                l = (l+r)//2 + 1
        if target <= nums[l]:
            return l
        if target > nums[l]:
            return l + 1
