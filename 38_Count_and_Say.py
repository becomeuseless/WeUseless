'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str

        Time Complexity : O(n^2)
        Space Complexity : O(n)
        """

        ##Recursion + Memoization(dictionary)

        dict = {}
        dict[1] = '1'
        if n in dict :
            return dict[n]
        else :
            s = self.countAndSay(n-1)
            l = len(s)
            temp = ''
            i = 0
            while i < l :
                if i < l - 1 :
                    j = 1
                    while i+j < l and s[i] == s[i+j] :
                        j += 1
                    temp = temp + str(j) + s[i]
                    i = i + j
                else :
                    temp = temp + '1' + s[i]
                    i += 1
            dict[n] = temp
            return temp
