# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        next_node = slow.next
        slow.next = None
        left, right = head, next_node
        prev = None
        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp

        left, right = head, prev
        while left and right:
            next_node = left.next
            next_prv = right.next
            right.next = None
            left.next = right
            right.next = next_node
            left = next_node
            right = next_prv

        






                

        
