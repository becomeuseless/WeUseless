"""
    Each iteration find a length of non repeating characters, move scan zone to next unrepeatable characters

    Example 1:

    Input: "abcabcbb" Output 3
    Input: "bbbbb" Output 1
    Input: "pwwkew" Output 3
    
    Space O(1) 	- distinct characters
    Time O(n)	- scan once
"""

class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s is None or len(s) == 0: return 0
        if len(s) == 1: return 1
        
        map = dict()                            # char - position map
        
        start = 0                               # scan start & end of the string
        end = 0
        curMax = 0
        
        for i in range(len(s)):
            index = map.get(s[i])                           #get existing index
            if index is not None and index >= start:        #dup char
                curMax = max(curMax, end-start)
                start = index + 1
                if curMax >= (len(s) - start):  # if rest of string short than curMax, end of search 
                    return curMax
            map[s[i]] = i                       #update the dictionary
            end += 1
            
        curMax = max(curMax, end-start) # if the string all unique
    
    