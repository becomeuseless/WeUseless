'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]




Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #Option1 : search p and q respectively, while searching them, store the ancestors in 2 lists, and then find the lowest
        #(the first from backwards) common ancestor.
        #Time Complextiy :  O(log n) worst O(n) if tree is unbalanced
        #Space Complecity :  O(log n) worst O(n) if tree is unbalanced
        '''
        cur = root
        pList = []
        while cur != p:
            pList.append(cur)
            if p.val < cur.val:
                cur = cur.left
            else :
                cur = cur.right
        pList.append(cur)

        cur = root
        qList = set()
        while cur != q:
            qList.add(cur)
            if q.val < cur.val:
                cur = cur.left
            else :
                cur = cur.right
        qList.add(cur)

        i = len(pList) - 1
        while i >= 0:
            if pList[i] in qList:
                return pList[i]
            i -= 1
            '''

        #Option2: Consider the BST's property, that for all nodes left to node N, the values are less than
        #the value of N, for all nodes right to node N, the values are greater than the value of N.
        #that means, given a node p and a node q, if p's value is smaller than a node N's value, q's value is
        #bigger than N's value. then N is the lowest common ancestor. Same conclusion if p'value is greater than
        #N'value and q's value is smaller than N's value. If p and q are both smaller or greater than N, then we
        #can move to N's left node(when p,q are smaller) or N's right node(when p,q are greater) to keep comparing.
        #Time Complextiy :  O(log n) worst O(n) if tree is unbalanced
        #Space Complecity :  O(log n) worst O(n) if tree is unbalanced
        '''
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
        '''
        #Option3: transfer option 2 to iterative solution
        #Time Compleixty: O(log n) if tree is balanced O(n) is tree is extremely unbalanced
        #Space Complexity : O(1)

        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        
