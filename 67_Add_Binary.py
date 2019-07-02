‘’‘
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
’‘’

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        num_a = int(a, base = 2)
        num_b = int(b, base = 2)

        return bin(num_a + num_b)[2:]
        
    def addBinary2(self, a: str, b: str) -> str:
        """
        Space:  O(n)
        Time:   O(n)
        
        Test cases: 
            "11" + "1"
            "11" +
                 + "1"
            "11" + "11"
            "1" + "11"
        """
        if not a:
            return b
        if not b:
            return a
        
        result = []
        listA = list(a)
        listB = list(b)
        carry = 0
        
        while listA and listB:
            newDigit = int(listA.pop()) + int(listB.pop()) + carry
            result.append(str(newDigit%2))
            carry = newDigit // 2
        
        while listA:
            newDigit = int(listA.pop()) + carry
            result.append(str(newDigit%2))
            carry = newDigit // 2
            
        while listB:
            newDigit = int(listB.pop()) + carry
            result.append(str(newDigit%2))
            carry = newDigit // 2
        
        if carry == 1:
            result.append(str(carry))
        
        return "".join([x for x in result[::-1]])   