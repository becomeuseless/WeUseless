'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        #Option 1: hash map and loop backwards
        #Time Complexity : O(n)
        #Space Complexity :O(n)
        m = {}
        m['A'] = 1
        m['B'] = 2
        m['C'] = 3
        m['D'] = 4
        m['E'] = 5
        m['F'] = 6
        m['G'] = 7
        m['H'] = 8
        m['I'] = 9
        m['J'] = 10
        m['K'] = 11
        m['L'] = 12
        m['M'] = 13
        m['N'] = 14
        m['O'] = 15
        m['P'] = 16
        m['Q'] = 17
        m['R'] = 18
        m['S'] = 19
        m['T'] = 20
        m['U'] = 21
        m['V'] = 22
        m['W'] = 23
        m['X'] = 24
        m['Y'] = 25
        m['Z'] = 26

        output = 0
        for i in range(len(s)):
            output += (26**i)*m[s[-i-1]]
        return output
        '''

        #Option 2: use ord() function and loop forwards:
        #Time Complexity : O(n)
        #Space Complexity :O(1)

        output = 0
        for l in s:
            output = output*26 + ord(l) - ord('A') + 1
        return output
