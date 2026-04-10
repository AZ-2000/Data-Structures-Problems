"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        if not head:
            return

        while curr:
            tmp = curr.next
            dummy = Node(curr.val)
            curr.next = dummy
            dummy.next = tmp
            curr = tmp

        curr = head

        while curr:
            tmp = curr.next.next
            if curr.random != None:
                curr.next.random = curr.random.next
            elif curr.random == None:
                curr.next.random = None
            curr = tmp

        curr = head
        head_cpy = head.next

        while curr:
            tmp = curr.next
            cpy = tmp.next.next if tmp.next else None
            skip = curr.next.next
            curr.next = skip
            tmp.next = cpy

            curr = skip

        return head_cpy
            
