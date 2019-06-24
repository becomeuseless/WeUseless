'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Option1 : we can do a loop of k and pop the end element and then insert to the top each step.
        #Time Complexity : O(n*k)
        #Space Complexity : O(1)

        #Option1 improved: we can slice the list at -k element and then insert the second sub-list to the top. One thing we
        #need to consider if k is bigger than n then we need to do k%n and then slice the list at -k%n.
        #Time Complexity : O(n)
        #Space Complexity : O(1)

        n = len(nums)
        nums[:] = nums[n-k%n:] + nums[:n-k%n]

        #be careful it can't be nums = nums[-k%n:] + nums[:k%n+1], because it will only change the reference, not the list itself.
