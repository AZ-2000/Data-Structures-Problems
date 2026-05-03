# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        count = 0
        dummy_tail = ListNode(0)
        dummy_tail.next = head
        old_tail = None

        while curr:
            count += 1
            curr = curr.next
        
        if count < k:
            return head
        else:
            curr = head
            groups = count // k
            flag = True

            if count % groups != 0:
                flag = False
            
            for grp in range(groups):
                j = 0
                if not flag and grp == groups:
                    break

                else:
                    prev = None
                    
                    while curr and j < k:
                        if j == 0:
                            tail = curr
                        tmp = curr.next
                        curr.next = prev
                        prev = curr
                        curr = tmp
                        j += 1 
                    if old_tail:
                        old_tail.next = prev
                    old_tail = tail
                    if grp == 0:
                        new_head = prev

                    prev = tail
                    prev.next = tmp

            return new_head


