'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        #Option 1 : Recursive, traverse all nodes
        #Time Complexity : O(n)
        #Space Complexity : O(n)
        if not root :
            return 0
        if root.left and root.right :
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
        if root.left:
            return self.minDepth(root.left) + 1
        if root.right:
            return self.minDepth(root.right) + 1
        if not root.left and not root.right :
            return 1
        '''


        #Option 2 : BFS + Queue
        #Time Complexity : O(n)
        #Space Complexity : O(n)
        if not root :
            return 0
        curLvl = [root]
        nxtLvl = []
        lvl = 1
        while len(curLvl) > 0:
            while len(curLvl) > 0:
                cur = curLvl.pop()
                if not cur.left and not cur.right:
                    return lvl
                if cur.left:
                    nxtLvl.insert(0,cur.left)
                if cur.right:
                    nxtLvl.insert(0,cur.right)
            curLvl = nxtLvl
            nxtLvl = []
            lvl += 1
