'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Option 1: loop thru the list. Time will be O(n), Space can be O(n/2)
        #Option 2: sort the list and then get the middle element. Time will be O(nlogn), space is O(1)
        #Option 3: there is this smart algorithm that does one pass with a O(1) space.

        majority, count = nums[0], 0
        for n in nums:
            if count == 0:
                majority, count = n, 1
            elif majority == n:
                count += 1
            else :
                count -= 1
        return majority
