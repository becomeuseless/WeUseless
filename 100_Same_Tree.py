'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        if (p and not q) or (not p and q) :
            return False
        elif p and q and p.val != q.val :
            return False
        elif not p and not q :
            return True
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #existing node
        if not p and not q:  #no child
            return True
        elif not p or not q: #not balanced
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
            return False
