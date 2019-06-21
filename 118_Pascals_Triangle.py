'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
        #Option 1 : loop array (Dynamic Programming)
        #Time Complexity : O(n^2)
        #Space Complexity : O(n^2)

        output = []
        for i in range(numRows) :
            output.append([])
            for j in range(i+1) :
                if j==0 :
                    output[-1].append(1)
                elif j==i :
                    output[-1].append(1)
                else :
                    output[-1].append(output[-2][j-1] + output[-2][j])
        return output
        '''

        #Option 2 : notice the pattern [0, 1, 3, 3, 1] + [1, 3, 3, 1, 0] = [1, 4, 6, 4, 1]
        #Time Complexity : O(n^2)
        #Space Complexity : O(n^2)

        output = [[1]]
        for i in range(numRows) :
            output += [map(lambda x, y : x+y, [0] + output[-1], output[-1] + [0])]
        return output[:numRows]
