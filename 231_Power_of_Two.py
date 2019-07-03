‘’‘
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
’‘’

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Option 1: keep dividing n by 2 and get its reminder, if the reminder ever not equal to 0 then n is not a power of 2.
        #Time Complexity : O(logn)
        #Space Complexity : O(1)
        '''
        if n == 0:
            return False
        while n != 1:
            if n%2 != 0:
                return False
            n = n/2
        return True
        '''

        #Option 2: treat the integer as a binary nubmer. If the binary number is a power of 2 then it will start with a 1
        #and followed by 0s. This kind of number can be detected by using bit manipulation.
        #Time Complexity : O(logn)
        #Space Complexity : O(1)
        return (n > 0) & (n & (n-1) == 0)
