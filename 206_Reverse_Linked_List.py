'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        # NULL <- 1 <- 2 <- 3  4 -> 5
        #Option 1: Recursive
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        if not head:
            return head
        return self.reverseNode(head,  None)

    def reverseNode(self, cur, pre):
        if not cur:
            return pre
        nxt = cur.next
        cur.next = pre
        return self.reverseNode(nxt, cur)
        '''

        #Option 2: Iterative
        #Time Complexity : O(n)
        #Space Complexity : O(1)

        if not head:
            return head

        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
