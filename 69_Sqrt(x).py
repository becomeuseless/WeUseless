'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ###return int(x ** 0.5)


        '''
        Binary Search
        Time Complexity : O(logn)
        Space Complexity : O(1)
        '''
        if x == 0 :
            return 0

        i = 1
        lo = i
        hi = x
        while hi - lo > 1 :
            if i * i <= x :
                lo = i
                i = (lo + hi) >> 1
            else :
                hi = i
                i = (lo + hi) >> 1
        return lo
