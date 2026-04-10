# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 1
        
        while curr.next:
            curr = curr.next
            length += 1

        if length == 1:
            head = None
            return head
        
        val = 0
        ind = length - n
        print(ind)
        prev = ListNode(0)
        prev.next = head
        curr = head
        while curr:
            if ind == 0:
                head = head.next
                break
            if val == ind:
                tmp = curr.next
                curr.next = None
                prev.next = tmp
                curr = tmp
                break
            val += 1
            prev = curr
            curr = curr.next

        return head
            

        