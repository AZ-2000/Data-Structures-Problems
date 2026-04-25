# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        fast = curr
        slow = curr
        while curr:
            if fast is None or fast.next is None:
                return False

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            curr = curr.next
    
        return False