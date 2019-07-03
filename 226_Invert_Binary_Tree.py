'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #Option 1: Depth First Search + Recursive
        #Time Complexity: O(n)
        #Space Complexity : O(n)
        '''
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        '''

        #Option 2 : Width First Search + queue
        #Time Complexity : O(n)
        #Space Completity : O(n)
        if not root:
            return
        myQueue = [root]
        while len(myQueue) > 0:
            p = myQueue.pop(0)
            if not p:
                continue
            myQueue.append(p.left)
            myQueue.append(p.right)
            temp = p.left
            p.left = p.right
            p.right = temp

        return root
