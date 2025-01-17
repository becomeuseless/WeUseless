"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

Time: O(n)
Space:O(1)

"""

class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x is None:
            return False
        return x == self.reverseNum(x)
    
    def reverseNum(self, x: int) -> int:
        """Previous Solution for reverse a number"""
        temp = abs(x)
        result = 0
        while temp > 0:
            result = result * 10 + temp % 10
            temp = temp // 10
            
        return result if x >= 0 else result * (-1)
      