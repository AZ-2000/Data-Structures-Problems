# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        curr = head
        prev = ListNode(0)
        prev.next = curr
        while curr:
            if curr.val == val:
                next_node = curr.next
                prev.next = next_node
                curr = next_node
                continue
            prev = curr
            curr = curr.next
        return head
            
        
