# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        dummy = ListNode(0)
        dummy.next = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next

        second = slow
        tmp = second.next
        dummy.next = None

        prev = None
        curr = second

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr = head
        rev = prev
        while curr and rev:
            if curr.val != rev.val:
                return False
            curr = curr.next
            rev = rev.next
        
        return True




        