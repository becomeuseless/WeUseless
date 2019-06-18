'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :Time Complexity : O(n)
        :Space Complexity : O(n)
        """
        if not root :
            return []

        curLvl = [root]
        nxtLvl = []
        output = []

        while len(curLvl) != 0 :
            output.insert(0,[])
            output[0] = [x.val for x in curLvl]
            while len(curLvl) != 0 :
                cur = curLvl.pop(0)
                if cur.left :
                    nxtLvl.append(cur.left)
                if cur.right :
                    nxtLvl.append(cur.right)
            curLvl = nxtLvl
            nxtLvl = []

        return output
