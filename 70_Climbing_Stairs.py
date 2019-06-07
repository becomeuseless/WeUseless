'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        #Option 1 : Recursion (slower) + Memoization
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        mydict = {}
        mydict[1] = 1
        mydict[2] = 2

        def recur(n):

            if n in mydict :
                return mydict[n]

            mydict[n] = recur(n-1) + recur(n-2)
            return mydict[n]

        return recur(n)
        '''

        #Option 2 : Iteration (faster)
        #Time Complexity : O(n)
        #Space Complexity : O(1)

        if n == 1 : return 1
        if n == 2 : return 2

        prev2 = 1
        prev1 = 2
        cur = 0

        for i in range(2,n) :
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur
