'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        test cases:
        ''
        ' '
        'Hello '
        'Hello'
        ' Hello World'

        Time Complexity O(m) m = length of the last word
        Space Complexity O(1)

        """
        if not s :
            return 0

        length = switch = i = 0

        while i < len(s) :
            if switch == 0 and s[-1-i] != ' ' :
                switch = 1
            if switch == 1 and s[-1-i] == ' ' :
                break
            if switch == 1 :
                length += 1
            i += 1
        return length
    
    
    def lengthOfLastWord2(self, s: str) -> int:
        count = 0
        strLen = len(s)
        metFirstAlph = False
        for i in range(strLen):
            each = s[strLen - 1 - i]
            if each != ' ':             #if each not a space
                count += 1
                metFirstAlph = True
            else:
                if metFirstAlph: #already a word
                    break
                else:
                    continue
        return count
    
    def lengthOfLastWord3(self, s: str) -> int:
        "[thing for thing in list_of_things if expression]"
        last_word = [word for word in s.split(' ') if word]
        if last_word:
            return len(last_word[-1])
        return 0
