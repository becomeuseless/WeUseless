'''Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1cur = l1
        l2cur = l2
        pre = None
        head = None

        if not l1 and l2 :
            return l2
        elif not l2 and l1 :
            return l1

        while l1cur and l2cur :
            if l1cur.val >= l2cur.val :
                if pre :
                    pre.next = l2cur
                else :
                    head = l2cur
                pre = l2cur
                l2cur = l2cur.next
            else :
                if pre :
                    pre.next = l1cur
                else :
                    head = l1cur
                pre = l1cur
                l1cur = l1cur.next

        if not l1cur and l2cur:
            pre.next = l2cur
        elif not l2cur and l1cur :
            pre.next = l1cur
        return head
            
