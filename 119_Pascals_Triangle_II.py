'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #Option 1 : Recursive
        #Time Complexity : O(n)
        #Space Complexity : O(n)
        if rowIndex == 0:
            return [1]
        PrevRow = self.getRow(rowIndex-1)
        return map(lambda x,y:x+y, [0] + PrevRow, PrevRow + [0])
