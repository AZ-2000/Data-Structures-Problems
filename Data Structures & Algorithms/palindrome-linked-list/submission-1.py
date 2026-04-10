# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length <= 1:
            return True
        if length == 2:
            curr = head
            if curr.val != curr.next.val:
                return False
            else:
                return True

        curr = head
        mid = length // 2
        i = 1
        while i <= length:
            if length %2 == 0:
                if i <= mid:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                    i += 1
                else:
                    if prev.val != curr.val:
                        return False
                    else:
                        prev = prev.next
                        curr = curr.next
                    i += 1
            elif length %2 != 0:
                if i == mid + 1:
                    curr = curr.next
                    i += 1
                if i <= mid:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                    i += 1
                else:
                    if prev.val != curr.val:
                        return False
                    else:
                        prev = prev.next
                        curr = curr.next
                    i += 1
        return True

        
