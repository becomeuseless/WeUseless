'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1 
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Because nonHappy numbers will loop endlessly in a cycle,we just need to store the numbers we have seen
        #and if ever we meet a number we have seen before and it's not 1, we know that it's entering into an cycle.
        #Time Complexity: O(1) It's been proved that the cycle is less than 8.
        #Space Complexity: O(1) It's been proved that the cycle is less than 8.
        seen = set()
        while n not in seen :
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        if n == 1:
            return True
        else:
            return False
