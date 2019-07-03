'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #use a hash map to store the characters seen in s, also use a set to store characters
        #seen in t, because this is going to be a 1-1 mapping.
        #Time Complexity : O(n)
        #Space Complexity : O(1)
        seen, used = {}, set()
        for i in range(len(s)):
            if s[i] in seen:
                if seen[s[i]] == t[i]:
                    continue
                else :
                    return False
            elif t[i] in used :
                return False
            else :
                seen[s[i]] = t[i]
                used.add(t[i])
        return True
