# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = list1
        curr2 = list2
        while curr and curr2:
            if curr.val < curr2.val:
                tail.next = curr
                curr = curr.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        if curr:
            tail.next = curr
        else:
            tail.next = curr2
        return dummy.next





