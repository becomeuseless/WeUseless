'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # to get this job done in logarithmic time, we can't comupte the facotrial because it would be at least O(n).
        # but notice to get a trailing zero, we need to mutiply 5(or multiples) and 2(or multiples). And how many trailing zeros
        # actually depends on how many 5s as factor there are. for example 10! would have two 5 facors as thre is a 5 and there is         # a 10. If we find how many 5s in the factorial we find how many trailing zeros.
        #Time Complexity : O(logn)
        #Space Complexity : O(1)

        cnt = 0
        while n > 0:
            n = n//5
            cnt += n
        return cnt
