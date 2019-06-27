'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        test cases:
        [1,2,3] => [1,2,4]
        [0] => [1]
        [1,9] => [2,0]
        [9,9] => [1,0,0]

        Time Complexity : best O(1) worst O(n)
        Space Complexity : O(1)
        """
        '''
        ### Option 1 : Iteration (faster)
        digits[-1] += 1

        i = 0
        for i in range(len(digits)) :
            if digits[-1-i] < 10 :
                break
            elif i+1 < len(digits) :
                digits[-1-i] = 0
                digits[-2-i] += 1
            else :
                digits.append(0)
                digits[0] = 1

        return digits
        '''

        ### Option 2 : Recursion (slower)
        '''
        Time Complexity : best O(1) worst O(n)
        Space Complexity : best O(1) worst O(n)
        '''
        if digits == [] :
            digits.append(1)
            return digits
        if digits[-1] + 1 < 10 :
            digits[-1] += 1
            return digits

        digits.pop()
        self.plusOne(digits)
        digits.append(0)
        return digits
    
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        [9,9,9] #need an insert if 9,9,9
        [0]
        [2,3,4]
        
        Time Complexity O(1)
        Space O(1)
        """
        
        digit = 0
        carry = 1
        
        for i in range(len(digits)):
            
            digit = digits[-1-i] + carry    #current digit
            digits[-1-i] = digit % 10      #new digit
            carry = digit // 10              #reset carry
            if carry == 0:
                break
        #check the first element at last if it is 0 then add 1
        if digits[0] == 0:
            digits.append(0)
            digits[0] = 1
            
        return digits
