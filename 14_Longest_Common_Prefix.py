"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        minLen = min([len(x) for x in strs])
        curPrefix = ""
        for i in range(minLen):
            curPrefix = strs[0][0:i+1]
            for each in strs:
                if each[0:i+1] != curPrefix:
                    return strs[0][0:i]
        return curPrefix    
        