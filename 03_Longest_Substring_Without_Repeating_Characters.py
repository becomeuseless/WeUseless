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

        def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0 : return 0
        elif l == 1 : return 1

        ## traverse the string from left to right, save the longest length and bound indexes when it reaches to a                 ## duplicate character, locate the ahead duplicate, make the charactor right next to it as the new left bound
        ## charactor. Repeat this process till to the end of the string.

        curL = 0    ## the left bound index of current substring in s
        curR = 0    ## the right bound index of current substring in s
        dup = -1     ## the ahead duplicate index in s
        curLength = 1
        longestLength = 1
        for i in range(1,l):
            for j in range(curL, i) :
                if s[j] == s[i] :
                    dup = j
                    break
            if dup != -1 :
                curL = dup + 1
                curLength = i - dup
                dup = -1
            else :
                curLength += 1
                longestLength = max(longestLength, curLength)
        return longestLength


