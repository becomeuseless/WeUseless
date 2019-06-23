'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Use two pointers that each starts from an end and compare the sum to the target, move the
        #pointers to shrink the list until the target sum is found or the list is empty.

        lo, hi = 0, len(numbers)-1
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo+1, hi+1]
            elif numbers[lo] + numbers[hi] > target:
                hi -= 1
            else :
                lo += 1
