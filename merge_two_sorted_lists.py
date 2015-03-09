# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        pointer = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            elif l1.val >l2.val:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1 != None:
            pointer.next = l1
        elif l2 != None:
            pointer.next = l2
        return head.next