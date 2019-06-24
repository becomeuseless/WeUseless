'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Option 1 : hash map
        #Time Complexity : O(n)
        #Space Complexity : O(n)

        #Option 2 : 2 pointers (fast pointer and slow pointer)
        #Time Complexity : O(n)
        #Space Complexity : O(1)
        '''
        if not head:
            return False

        pfast = pslow = head
        while pfast.next and pfast.next.next :
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                return True
        return False
        '''

        #Option 2 improved : 2 pointers and use exception
        #Time Complexity : O(n)
        #Space Complexity : O(1)

        try :
            pslow, pfast = head, head.next
            while pfast != pslow:
                pfast = pfast.next.next
                pslow = pslow.next
            return True
        except :
            return False
