'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Option 1 : Recursive
        #Time Complexity : O(n^2)
        #Space Complexity : O(n^2)

        '''
        if not root :
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.treeHeight(root.left) - self.treeHeight(root.right)) < 2 :
            return True
        else :
            return False

    def treeHeight(self, root):
        if not root :
            return -1
        return max(self.treeHeight(root.left), self.treeHeight(root.right)) + 1
        '''

        #Option 2: Recursive improved version. This version uses a flag to determine if a sub-tree is balanced.
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        if not root :
            return True
        if self.helper(root) != -1 :
            return True
        else :
            return False

    def helper(self, root):
        if not root :
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == - 1 or abs(left - right) > 1 :
            return -1
        else :
            return max(left, right) + 1
