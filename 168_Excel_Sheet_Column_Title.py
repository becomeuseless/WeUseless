'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        #the math is treat this as 26-ary. The only thing needs to be careful is there is no Zero in this 26-ary.
        #Time Complexity : O(logn) ???
        #Space Complexity : O(1)

        Capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]

        output = ''

        while n != 0:
            output = Capitals[(n-1)%26] + output
            n = (n - 1)//26
        return output
