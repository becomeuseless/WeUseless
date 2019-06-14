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


    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        if not l1 and l2:
            return l2
        dummy = ListNode(0)
        iter1 = l1
        iter2 = l2
        iterMerge = dummy
        # if l1 and l2 both not null
        while iter1 and iter2:
            if iter1.val <= iter2.val:
                iterMerge.next = iter1
                iterMerge = iterMerge.next
                iter1 = iter1.next
            else:
                iterMerge.next = iter2
                iterMerge = iterMerge.next
                iter2 = iter2.next
        # one list is emtpy
        if iter1:
            iterMerge.next = iter1
        
        if iter2:
            iterMerge.next = iter2
        
        return dummy.next

# Copy from most proficient answer
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


                    
            
            	
            
