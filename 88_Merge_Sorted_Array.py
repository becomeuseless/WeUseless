'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        '''
        ### Option 1 : fill nums1 from start to end
        ### Time Complexity : O(n*m)
        ### Space Complexity : O(1)
        i = 0
        curLen = m
        for item in nums2 :
            while i < curLen and item > nums1[i] :
                i += 1

            j = curLen
            while j > i :
                nums1[j] = nums1[j - 1]
                j -= 1
            nums1[i] = item
            curLen += 1
        '''

        ### Option 2 : fill nums1 from end to start
        ### Time Complexity : O(n+m)
        ### Space Complexity : O(1)

        while m > 0 and n > 0 :
            if nums1[m-1] > nums2[n-1] :
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else :
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        while n > 0 : ## if nums1 reaches to the left but nums2 got more to fill
            nums1[m+n-1] = nums2[n-1]
            n -= 1
            
