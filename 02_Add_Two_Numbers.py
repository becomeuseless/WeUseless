"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        l1 = 2 -> 4 -> 3
        l2 = 5 -> 6 -> 4
        nums1 = 243
        nums2 = 564
        """
        carry = 0
        dummy = ListNode(0)
        iter = dummy
        
        iter1 = l1
        iter2 = l2
        total = 0
        
        while True:
            if iter1 is not None and iter2 is not None:
                total = iter1.val + iter2.val + carry
                carry = total // 10
                iter1 = iter1.next
                iter2 = iter2.next
            elif iter1 is not None:
                total = iter1.val + carry
                carry = total // 10
                iter1 = iter1.next
            elif iter2 is not None:
                total = iter2.val + carry
                carry = total // 10
                iter2 = iter2.next
            else:
                if carry == 1:
                    iter.next = ListNode(1)
                break
            iter.next = ListNode(total % 10)
            iter = iter.next  

        return dummy.next