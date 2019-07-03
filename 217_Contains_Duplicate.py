'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Option 1 : traverse every item in nums, check all the following items if there is a duplicate.
        #Time Complexity : worst O(n**2), best O(1)
        #Space Complexity: O(1)

        #Option 2: use a set, traverse every item in nums, whenever see a new item, add it into a set, return when see a duplicate
        #Time Complexity : worst O(n), best O(1)
        #Space Complexity : worst O(n), best O(1)
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else :
                seen.add(i)
