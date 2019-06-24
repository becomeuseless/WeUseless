'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        #Option 1 : loop and compare, skip non-alphanumeric charactors
        #Time Complexity : O(n)
        #Space Complexity : O(1)
        i, j = 0, len(s)-1
        while i < j :
            if not s[i].isalnum():
                i += 1      #left point move right if current is not alphanumeric
                continue
            if not s[j].isalnum():
                j -= 1      #right point move left if current is not alphanumeric
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        '''

        #Option 2 : create a list to store alphanumeric characters.
        #Time Complexity : O(n)
        #Space Complexity : O(n)
        myList = [a.lower() for a in s if a.isalnum()]
        return myList == myList[::-1]
