'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #Option 1: traverse all items in the list and for every item, look for duplicates in following k items
        #Time Complexity : O(n*k)
        #Space Complexity : O(1)
        '''
        for i in range(len(nums)):
            j = 1
            while i + j < len(nums) and j < k + 1:
                if nums[i] == nums[i+j]:
                    return True
                j += 1
        return False
        '''
        #Option 2: use a hash table, traverse the list and if the item not seen before, add it to the hash table with it location.
        #When see an item that was seen before, caculate the distance, if smaller than k, return True, if bigger than k, update the
        #position of that item.
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            else :
                seen[nums[i]] = i
        return False
