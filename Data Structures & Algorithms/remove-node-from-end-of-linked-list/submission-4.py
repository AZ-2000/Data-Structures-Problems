# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
        dummy = ListNode(0)
        
        if not curr.next:
            return 
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr = prev

        for i in range(1,n-1):
            # print("here", curr.val)
            curr = curr.next
        if n == 1:
            prev = curr.next
        else:
            curr.next = curr.next.next

        dummy.next = prev
        prev_2 = None
        curr = prev
        while curr:
            tmp = curr.next
            curr.next = prev_2
            prev_2 = curr
            curr = tmp
        dummy.next = prev_2
        return dummy.next
            
            