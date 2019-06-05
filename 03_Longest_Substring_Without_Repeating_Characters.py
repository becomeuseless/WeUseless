"""
    Each round find a length of non repeating characters, cut it and pass to the same function

    Example 1:

    Input: "abcabcbb" Output 3
    Input: "bbbbb" Output 1
    Input: "pwwkew" Output 3
    

"""

class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        def helpSearch(s: str, curmax) -> int:
            """
                Help search only leading non repeatable length, if curmax >= rest of unscanned, quit
            """
            #base case
            if len(s) == 1:
                return 1

            # if current max >= string length left, then quit search
            if curmax >= len(s):
                return curmax

            elements = set()
            no_dup_length = 0

            for each in s:
                if each in elements:
                    break
                else:
                    elements.add(each)
                    no_dup_length += 1

            return max(no_dup_length, helpSearch(s[1:], max(curmax, no_dup_length)))
    
        if s is None:
            return 0
        return helpSearch(s,curmax=0)
    
    