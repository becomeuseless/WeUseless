'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Option 1 : Recursion
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        if not root :
            return True
        if not root.left and not root.right :
            return True
        def isMirror(p, q):
            if not p and not q :
                return True
            if not p or not q :
                return False
            return isMirror(p.left, q.right) and isMirror(p.right, q.left) and p.val == q.val

        return isMirror(root.left, root.right)

         """
        Option 2 : Iteration
        Time Complexity : O(n)
        Space Complexity : O(1)

        if not root :
            return True
        if not root.left and not root.right :
            return True
        if not root.left or not root.right :
            return False
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) != 0 :
            p = queue.pop()
            q = queue.pop()
            if not p and not q:
                continue
            if not p or not q :
                return False
            if p.val != q.val :
                return False
            queue.insert(0, p.left)
            queue.insert(0, q.right)
            queue.insert(0, p.right)
            queue.insert(0, q.left)
        return True
        """
