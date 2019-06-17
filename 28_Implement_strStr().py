'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

strStr2 is brutal force. Time: O(n * m), Space: O(1)

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Time Complexity : O(n)
        #Space Complexity : O(1)

        i = 0
        li = len(haystack)
        lj = len(needle)
        if lj == 0 :
            return 0

        while i < li - lj + 1:
            j = 0
            while j < lj and i + j < li and haystack[i+j] == needle[j] :
                j += 1
            if j == lj :
                    return i
            i += 1
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            for j in range(len(needle)):
                #check if rest of haystack is not enough
                if len(haystack) - i < len(needle) - j:
                    return -1      
                furtherStepGoes = 0
                jumpIfFailed = 0
                if haystack[i] == needle[j]:
                    if haystack[i] == needle[0]:
                        jumpIfFailed = i
                    furtherStepGoes += 1
                    i = i + 1
                    j = j + 1
                    if j == len(needle):
                        return i - len(needle)
                    continue
                if haystack[i] != needle[j]:
                    #rollback and goes to next character
                    i = jumpIfFailed + 1
                    j = 1
                    break
        return -1
        
